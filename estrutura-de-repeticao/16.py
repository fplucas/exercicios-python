fibonacci = [1, 1]
x = 2
while(fibonacci[x - 1] < 500):
    numero = fibonacci[x - 1] + fibonacci[x - 2]
    fibonacci.append(numero)
    x += 1

print(fibonacci)