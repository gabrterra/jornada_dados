# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num_1 = int(input("Digite um numero: "))
num_2 = int(input("Digite outro numero: "))
print(num_1 + num_2)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input("Digite um numero: "))
print(num % 5)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num_1 = int(input("Digite um numero: "))
num_2 = int(input("Digite outro numero: "))
print(num_1 * num_2)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num_1 = int(input("Digite um numero: "))
num_2 = int(input("Digite outro numero: "))
print(num_1 // num_2)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num_1 = int(input("Digite um numero: "))
print(num_1 ** 2)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num_1 = float(input("Digite um numero: "))
num_2 = float(input("Digite outro numero: "))
print(num_1 + num_2)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num_1 = float(input("Digite um numero: "))
num_2 = float(input("Digite outro numero: "))
print((num_1 + num_2) / 2)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
num_1 = float(input("Digite um numero: "))
num_2 = float(input("Digite outro numero: "))
print(num_1 ** num_2)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
num_1 = float(input("Digite um numero: "))
print((num_1 * 1.8) + 32)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
num_1 = float(input("Digite um numero: "))
print(math.pi * (num_1 ** 2))

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
str_1 = input("Digite um texto: ")
print(str_1.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
str_1 = input("Digite um texto: ")
print(str_1.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
str_1 = input("Digite um texto: ")
print(str_1.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data_input = input("Digite uma data no formato dd/mm/aaaa: ")
lista_data = data_input.split("/")
dia = lista_data[0]
mes = lista_data[1]
ano = lista_data[2]
print(f"dia: {dia}, mês: {mes}, ano: {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
str_1 = input("Digite um texto: ")
str_2 = input("Digite outro texto: ")
print(str_1 + str_2)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação