# Programa: Tabuada

# Pede para o usuário digitar um número
numero = int(input("Digite um número para ver a tabuada: "))

# Laço de repetição de 1 até 10
for i in range(1, 10 + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
