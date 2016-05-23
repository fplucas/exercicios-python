quantidade_de_pessoas = int(input('Entre com a quantidade de pessoas: '))

idades = []
for idade in range(0, quantidade_de_pessoas):
    idades.append(int(input(
        'Entre com a idade da {}a. pessoa: '.format(idade + 1))))

media = sum(idades) / len(idades)

if(media <= 25):
    print('A média de idade é jovem!')
elif(media <= 60):
    print('A média de idade é adulta!')
else:
    print('A média de idade é idosa!')