contador = int(input('Quantos números na sequência Fibonacci deseja gerar? '))
fibonacci = [1, 1]
for x in range(2, contador):
    numero = fibonacci[x - 1] + fibonacci[x - 2]
    fibonacci.append(numero)

print(fibonacci)