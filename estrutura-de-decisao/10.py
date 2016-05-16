turno = input('Em qual turno você estuda? M - matutino / V - vespertino / N - noturno\n').upper()
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido!')