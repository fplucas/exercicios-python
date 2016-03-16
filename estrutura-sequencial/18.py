print('Entre com o tamanho do arquivo em Mb')
arquivo = float(input())
print('Entre com a velocidade da internet em Mbps')
velocidade = float(input())
tempo = arquivo / velocidade
segundos = tempo
minutos = 0
while segundos >= 60:
    segundos -= 60
    minutos += 1
print('O arquivo será baixado em %s minutos e %s segundos' % (minutos, segundos))