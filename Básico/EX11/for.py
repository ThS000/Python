numero = int(input("Digite um número: "))

while numero > 10:
    print("O número não pode ser maior que 10.")
    numero = int(input("Digite um número novamente: "))

for i in range(numero, 11):
    print(i)