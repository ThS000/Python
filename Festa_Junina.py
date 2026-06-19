quantidade = int(input())

numeros = input().split()

resultado = 0

for i in range(quantidade):
    numero = int(numeros[i])

    if i % 2 == 0:
        resultado += numero
    else:
        resultado -= numero

if resultado < 0:
    resultado = -resultado

print(resultado)