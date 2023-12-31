# datasus-fetcher

This package function is to download DATASUS raw data files (DBC) from its
FTP server. It does not have reading functions.

Online queries: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/

Microdata: https://datasus.saude.gov.br/transferencia-de-arquivos/

- Base Populacional - IBGE
  - BASE-POPULACIONAL-IBGE-POP: Censo e Estimativas
  - BASE-POPULACIONAL-IBGE-POPT: Estimativas TCU
- Base Territorial - Mapas e conversões para tabulação
  - Base Territoriais
  - Mapas
  - Conversões
- CIH: Sistema de Comunicação de Informação Hospitalar
  - CIH-CR: Comunicação de Internação Hospitalar
- CIHA: Sistema de Comunicação de Informação Hospitalar e Ambulatorial
  - CIHA-CIHA: Sistema de Comunicação de Informação Hospitalar e Ambulatorial
- CNES: Cadastro Nacional de Estabelecimentos de Saúde
  - CNES-LT: Leitos
  - CNES-ST: Estabelecimentos
  - CNES-DC: Dados Complementares
  - CNES-EQ: Equipamentos
  - CNES-SR: Serviço Especializado
  - CNES-HB: Habilitação
  - CNES-PF: Profissional
  - CNES-EP: Equipes
  - CNES-RC: Regra Contratual
  - CNES-IN: Incentivos
  - CNES-EE: Estabelecimento de Ensino
  - CNES-EF: Estabelecimento Filantrópico
  - CNES-GM: Gestão e Metas
- PCE: Programa de Controle da Esquistossomose
  - PCE-PCE: Programa de Controle da Esquistossomose
- PO: Painel de Oncologia
  - PO-PO: Painel de Oncologia
- RESP: Notificações de casos suspeitos de SCZ
  - RESP: Notificações de casos suspeitos de SCZ
- SIA: Sistema de Informações Ambulatoriais
  - SIA-AB: APAC de Acompanhamento a Cirurgia Bariátrica
  - SIA-ABO: APAC Acompanhamento Pós Cirurgia Bariátrica
  - SIA-ACF: APAC Confeção de Fístula Arteriovenosa
  - SIA-AD: APAC de Laudos Diversos
  - SIA-AM: APAC de Medicamentos
  - SIA-AN: APAC de Nefrologia
  - SIA-AQ: APAC de Quimioterapia
  - SIA-AR: APAC de Radioterapia
  - SIA-ATD: APAC de Tratamento Dialítico
  - SIA-PA: Produção Ambulatorial
  - SIA-PS: Psicossocial
  - SIA-SAD: Atenção Domiciliar
- SIH: Sistema de Informação Hospitalar (Descentralizado)
  - SIH-RD: AIH Reduzida
  - SIH-RJ: AIH Rejeitadas
  - SIH-SP: Serviços Profissionais
  - SIH-ER: AIH Rejeitadas com código de erro
- SIM: Sistema de Informação de Mortalidade
  - SIM-DO: Declarações de Óbito
  - SIM-DOEXT: Declarações de Óbitos por causas externas
  - SIM-DOFET: Declarações de Óbitos fetais
  - SIM-DOINF: Declarações de Óbitos infantis
  - SIM-DOMAT: Declarações de Óbitos maternos
  - SIM-DOREXT: Mortalidade de residentes no exterior
- SINAN: Sistma de agravos de notificação compulsória
  - SINAN-ACBI: Acidente de trabalho com material biológico
  - SINAN-ACGR: Acidente de trabalho
  - SINAN-ANIM: Acidente por Animais Peçonhentos
  - SINAN-ANTR: Atendimento Antirrabico
  - SINAN-BOTU: Botulismo
  - SINAN-CANC: Cancêr relacionado ao trabalho
  - SINAN-CHAG: Doença de Chagas Aguda
  - SINAN-CHIK: Febre de Chikungunya
  - SINAN-COLE: Cólera
  - SINAN-COQU: Coqueluche
  - SINAN-DENG: Dengue
  - SINAN-DERM: Dermatoses ocupacionais
  - SINAN-DIFT: Difteria
  - SINAN-ESQU: Esquistossomose
  - SINAN-EXAN: Doenças exantemáticas
  - SINAN-FMAC: Febre Maculosa
  - SINAN-FTIF: Febre Tifóide
  - SINAN-HANS: Hanseníase
  - SINAN-HANT: Hantavirose
  - SINAN-HEPA: Hepatites Virais
  - SINAN-IEXO: Intoxicação Exógena
  - SINAN-INFL: Influenza Pandêmica
  - SINAN-LEIV: Leishmaniose Visceral
  - SINAN-LEPT: Leptospirose
  - SINAN-LERD: LER/Dort
  - SINAN-LTAN: Leishmaniose Tegumentar Americana
  - SINAN-MALA: Malária
  - SINAN-MENI: Meningite
  - SINAN-MENT: Transtornos mentais relacionados ao trabalho
  - SINAN-NTRA: Notificação de Tracoma
  - SINAN-PAIR: Perda auditiva por ruído relacionado ao trabalho
  - SINAN-PEST: Peste
  - SINAN-PFAN: Paralisia Flácida Aguda
  - SINAN-PNEU: Pneumoconioses relacionadas ao trabalho
  - SINAN-RAIV: Raiva
  - SINAN-SDTA: Surto Doenças Transmitidas por Alimentos
  - SINAN-SIFA: Sífilis Adquirida
  - SINAN-SIFC: Sífilis Congênita
  - SINAN-SIFG: Sífilis em Gestante
  - SINAN-SRC: Síndrome da Rubéola Congênia
  - SINAN-TETA: Tétano Acidental
  - SINAN-TETN: Tétano Neonatal
  - SINAN-TOXC: Toxoplasmose Congênita
  - SINAN-TOXG: Toxoplasmose Gestacional
  - SINAN-TRAC: Inquérito de Tracoma
  - SINAN-TUBE: Tuberculose
  - SINAN-VARC: Varicela
  - SINAN-VIOL: Violência doméstica, sexual e/ou outras violências
  - SINAN-ZIKA: Zika Vírus
- SINASC: Sistema de Informação de Nascidos Vivos
  - SINASC-DN: Declarações de nascidos vivos 1994 a 2020
  - SINASC-DNEX: Declarações de nascidos vivos no exterior 2014 a 2020
- SISCOLO: Sistema de Informações de Cânceres de Colo de Útero
  - SISCOLO-CC: Citopatológico de Colo de Útero
  - SISCOLO-HC: Histopatológico de Colo de Útero
- SISMAMA: Sistema de Informações de Cânceres de Mama
  - SISMAMA-CM: Citopatológico de Mama
  - SISMAMA-HC: Histopatológico de Mama
- SISPRENATAL: Sistema de Monitoramento e Avaliação do Pré-Natal, Parto, Puepério e Criança
  - SISPRENATAL-PN: Pré-Natal

## Development

Install development version from Github running this command:

```sh
pip install -e git+https://github.com/viridisdata/datasus-fetcher.git
```

Run unit tests with:

```sh
python -m unittest discover
```
