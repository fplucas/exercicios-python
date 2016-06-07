numeros_entre_0_e_25 = 0
numeros_entre_26_e_50 = 0
numeros_entre_51_e_75 = 0
numeros_entre_76_e_100 = 0
while(True):
    numero = int(input('Entre com um número: '))
    if(numero < 0):
        break
    elif(numero <= 25):
        numeros_entre_0_e_25 += 1
    elif(numero <= 50):
        numeros_entre_26_e_50 += 1
    elif(numero <= 75):
        numeros_entre_51_e_75 += 1
    elif(numero <= 100):
        numeros_entre_76_e_100 += 1

print('Números entre 0 e 25: {}'.format(numeros_entre_0_e_25))
print('Números entre 26 e 50: {}'.format(numeros_entre_26_e_50))
print('Números entre 51 e 75: {}'.format(numeros_entre_51_e_75))
print('Números entre 76 e 100: {}'.format(numeros_entre_76_e_100))
