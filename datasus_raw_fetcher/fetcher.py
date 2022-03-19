import datetime as dt
import ftplib
import pathlib
import re
import time

from . import meta
from .storage import get_filename, get_sha1_hash

FTP_HOST = "ftp.datasus.gov.br"


def connect() -> ftplib.FTP:
    """Connects to the FTP server."""
    ftp = ftplib.FTP(FTP_HOST, encoding="latin-1")
    ftp.login()
    return ftp


def list_files(ftp: ftplib.FTP) -> list:
    """List all files in the current directory."""
    files = []
    pwd = ftp.pwd()
    ftp.retrlines("LIST", files.append)
    # parse files' date, size and name
    files = [
        {
            "datetime": dt.datetime.strptime(date + " " + time, "%m-%d-%y %I:%M%p"),
            "size": int(size),
            "name": name,
            "full_path": pwd + "/" + name,
        }
        for date, time, size, name in map(str.split, files)
    ]
    return files


def fetch_file(
    ftp: ftplib.FTP,
    path: str,
    dest_filepath: pathlib.Path | str,
) -> str:
    """Fetch a file from a remote FTP server.

    :param path: The path to the file.
    :param dest_filepath: The destination file path.
    :param ftp: The FTP connection.
    """

    if isinstance(dest_filepath, str):
        dest_filepath = pathlib.Path(dest_filepath.lower())
    if not dest_filepath.parent.exists():
        dest_filepath.parent.mkdir(parents=True)

    try:
        with open(dest_filepath, "wb") as f:
            ftp.retrbinary("RETR " + path, f.write)
        sha1 = get_sha1_hash(dest_filepath)
        return sha1
    except ftplib.error_perm:
        print(f"File {path} not found.")
        dest_filepath.unlink()


def get_year2(year_: str) -> int:
    if year_[0] in "789":
        year = 1900 + int(year_)
    else:
        year = 2000 + int(year_)
    return year


def parse_uf_year2_month_filename(match: re.Match) -> dict:
    uf = match.group(1)
    year_ = match.group(2)
    year = get_year2(year_)
    month = int(match.group(3))
    return {
        "uf": uf,
        "year": year,
        "month": month,
    }


def parse_year_filename(match: re.Match) -> dict:
    year = int(match.group(1))
    return {
        "year": year,
    }


def parse_year2_filename(match: re.Match) -> dict:
    year_ = match.group(1)
    year = get_year2(year_)
    return {
        "year": year,
    }


def parse_uf_year_filename(match: re.Match) -> dict:
    uf = match.group(1)
    year = int(match.group(2))
    return {
        "uf": uf,
        "year": year,
    }


def parse_uf_year2_filename(match: re.Match) -> dict:
    uf = match.group(1)
    year_ = match.group(2)
    year = get_year2(year_)
    return {
        "uf": uf,
        "year": year,
    }


def parse_filename(match: re.Match, pattern: str) -> dict:
    match pattern:
        case meta.uf_year_pattern:
            return parse_uf_year_filename(match)
        case meta.uf_year2_pattern:
            return parse_uf_year2_filename(match)
        case meta.uf_year2_month_pattern:
            return parse_uf_year2_month_filename(match)
        case meta.year_pattern:
            return parse_year_filename(match)
        case meta.year2_pattern:
            return parse_year2_filename(match)


def list_dataset_files(ftp: ftplib.FTP, dataset: str) -> dict:
    for period in meta.datasets[dataset]["periods"]:
        ftp.cwd(period["dir"])
        files = list_files(ftp)
        fn_prefix = period["filename_prefix"]
        fn_pattern = period["filename_pattern"]
        pattern = re.compile(f"^{fn_prefix}{fn_pattern}\\.dbc$".lower())
        for file in files:
            m = pattern.match(file["name"].lower())
            if m:
                try:
                    file |= parse_filename(m, fn_pattern)
                except:
                    print("Parsing error:", file, fn_pattern)
                    raise
                yield file


def download_dataset(ftp: ftplib.FTP, dataset: str, destdir: pathlib.Path):
    partition = meta.datasets[dataset]["partition"]
    i = 0
    for file in list_dataset_files(ftp, dataset):
        filepath = destdir / dataset / get_filename(file, partition)
        if filepath.exists():
            if filepath.stat().st_size == file["size"]:
                continue
            continue
        elif not filepath.parent.exists():
            filepath.parent.mkdir(parents=True)
        print(f"{i: >5}", file["full_path"], "->", filepath)
        t0 = time.time()
        sha1 = fetch_file(ftp, file["full_path"], filepath)
        tt = time.time() - t0
        print(
            sha1,
            f"{tt:.2f} s",
            f"{file['size'] / 1024:.2f} kB",
            f"{file['size'] / tt / 1024:.2f} kB/s",
        )
        i += 1