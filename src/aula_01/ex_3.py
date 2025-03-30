## Calculo do Bonus

CONSTANTE_BONUS = 1000

#solicita ao user que digite seu nome
nome = input("Digite seu nome: ")
print("Ola ",nome,"!")

#solicita ao user que digite seu salário
salario = float(input("Digite seu salario: "))
print("Seu salario é: ",salario)

#solicita ao user que digite o bônus recebido
bonus = float(input("Digite o bonus %: "))/100
print("Seu bonus foi: ",bonus)

#calcular o salário final
salario_final = salario + (CONSTANTE_BONUS+ salario * bonus)
print("Seu salario final: ",salario_final)

#mensagem personalizada (nome, salario, bônus)
print(f"Ola {nome}, seu salario foi: {salario}, seu bonus foi: {bonus}, seu salario final: {salario_final}")

#quantos bugs e riscos você consegue identificar nesse programa? 