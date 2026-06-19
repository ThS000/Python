num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

numMaior = num1

if num2 > numMaior:
    numMaior = num2

if num3 > numMaior:
    numMaior = num3

print(f"O maior número é {numMaior}")