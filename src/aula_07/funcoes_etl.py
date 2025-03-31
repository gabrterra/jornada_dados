import csv

def ler_csv(diretorio_arquivo_csv: str) -> list[dict]:
    """ 
    Função para ler um arquivo scv e retorna uma lista de dicionarios
    """
    with open(diretorio_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
    return list(leitor)

vendas_intes = list[dict]

