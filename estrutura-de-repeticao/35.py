divisoes = 0

def eh_primo(numero, divisoes):
    primo = True
    for x in range(2, numero):
        divisoes += 1
        if(numero % x == 0):
            primo = False
    return primo, divisoes

primos = []
numero = int(input('Entre com um número: '))
for x in range(1, numero):
    primo, divisoes = eh_primo(x, divisoes)
    if(primo):
        primos.append(x)

print('Números primos entre 1 e {}: {}'.format(numero, primos))
print('Total de divisões: {}'.format(divisoes))