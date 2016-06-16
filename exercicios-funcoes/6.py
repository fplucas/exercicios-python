def verifica_validade_do_horario(horas, minutos):
    if(horas < 0 or horas >= 24 or minutos < 0 or minutos >= 60):
        print('Entre com um horário válido')
        return True
    else:
        return False

continua = True
while(continua):
    horario_invalido = True
    while(horario_invalido):
        horario = input('Entre com o horário em formato 24 horas (ex: 23:45): ')
        horario = horario.split(':')
        horas = int(horario[0])
        minutos = int(horario[1])
        horario_invalido = verifica_validade_do_horario(horas, minutos)
    if(horas <= 12):
        periodo = 'AM'
    else:
        horas -= 12
        periodo = 'PM'
    print('Horário em formato AM/PM: {}:{} {}'.format(horas, minutos, periodo))
    resposta = input('Deseja continuar? s/n: ').upper()
    if(resposta != 'S'):
        continua = False