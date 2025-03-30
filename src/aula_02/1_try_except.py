try:
    resultado = len(3)
    print(resultado)
except TypeError as e:
    print(e)
else:
    print("deu certo")
finally:
    print("acabou")