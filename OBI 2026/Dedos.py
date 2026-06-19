soma = 0

minimo = int(input())
anelar = int(input())
medio = int(input())
indicador = int(input())
polegar = int(input())

if minimo == 1:
    soma = soma + 16
else:
    soma = soma + 0

if anelar == 1:
    soma = soma + 8
else:
    soma = soma + 0

if medio == 1:
    soma = soma + 4
else:
    soma = soma + 0

if indicador == 1:
    soma = soma + 2
else:
    soma = soma + 0

if polegar == 1:
    soma = soma + 1
else:
    soma = soma + 0

print(soma)