print('Entre com um número inteiro')
primeiro_numero_inteiro = int(input())
print('Entre com o segundo número inteiro')
segundo_numero_inteiro = int(input())
print('Entre com um número real')
numero_real = float(input())
resultado_a = (primeiro_numero_inteiro * 2) * (segundo_numero_inteiro / 2)
print('O produto do dobro do primeiro com metade do segundo é %s' % resultado_a)
resultado_b = (primeiro_numero_inteiro * 3) + numero_real
print('A soma do triplo do primeiro com o terceiro é %s' % resultado_b)
resultado_c = numero_real ** 3
print('O terceiro elevado ao cubo é %s' % resultado_c)