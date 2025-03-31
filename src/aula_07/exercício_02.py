# Filtrar Dados Acima de um Limite

from typing import List

def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    """
    Filtra os valores acima de um limite especificado.
    Args:
        valores (List[float]): Lista de valores a serem filtrados.
        limite (float): Limite acima do qual os valores serão filtrados.
    Returns:
        List[float]: Lista de valores acima do limite.
    """
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado


lista = [5,6,8,23,87,23,665,665,89,54,7,90,5,7,9,66,8,9]

limite = 10

filtrado = filtrar_acima_de(lista, limite)

# ordernar lista, sem que retorne
filtrado = sorted(filtrado, reverse=False)

# remover duplicados do filtrado:
filtrado = list(dict.fromkeys(filtrado))

# remover dulpicadas da lista original:
lista = list(dict.fromkeys(lista))


print(filtrado)