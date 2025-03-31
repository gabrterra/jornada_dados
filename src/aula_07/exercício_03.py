# Contar Valores Únicos em uma Lista

from typing import List

def contar_valores_unicos(lista: List[int]) -> int:
    """
    Conta o número de valores únicos em uma lista.
    
    Args:
        lista (List[int]): Lista de inteiros.
        
    Returns:
        int: Número de valores únicos na lista.
    """
    return len(set(lista))

lista = [5, 6, 8, 23, 87, 23, 665, 89, 54, 7, 90, 5, 87, 66, 66, 8, 9]

print(contar_valores_unicos(lista))