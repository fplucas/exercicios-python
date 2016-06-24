def obtem_ips():
    arquivo = open('ips.txt', 'r')
    conteudo = arquivo.read()
    ips = conteudo.split('\n')
    arquivo.close()
    return ips

def valida_ip(ip):
    partes = ip.split('.')
    for parte in partes:
        if(int(parte) < 0 or int(parte) > 255):
            return False
    return True

def grava_ips(ips):
    conteudo = ''
    for ip in ips:
        conteudo += '{}\n'.format(ip)
    return conteudo

def cria_arquivo(ips_validos, ips_invalidos):
    arquivo = open('saida.txt', 'w')
    arquivo.write('[Endereços válidos:]\n')
    arquivo.write(grava_ips(ips_validos))
    arquivo.write('\n[Endereços inválidos:]\n')
    arquivo.write(grava_ips(ips_invalidos))
    arquivo.close()

ips_validos = []
ips_invalidos = []
ips = obtem_ips()
for ip in ips:
    ip_valido = valida_ip(ip)
    if(ip_valido):
        ips_validos.append(ip)
    else:
        ips_invalidos.append(ip)

cria_arquivo(ips_validos, ips_invalidos)