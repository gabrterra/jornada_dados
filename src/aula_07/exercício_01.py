# Calcular Média de Valores em uma Lista

from typing import List
def media_valores(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    return media

lista = [5,6,8,23,87,23,665,89,54,7,90,5,7,9,66,8,9]

print(media_valores(lista))