alfabeto ={'A': '@', 'B': '|3', 'C': '<', 'D': '|>', 'E': '3', 'F': '|=', 'G': '6', 'H': '#', 'I': '1', 'J': '_/', 'K': '|<', 'L': '1', 'M': '|\/|', 'N': '|\|', 'O': '0', 'P': '|^', 'Q': '9', 'R': 'P\\', 'S': '$', 'T': '7', 'U': '(_)', 'V': 'V', 'W': '\/\/', 'X': '><', 'Y': '`/', 'Z': '2'}

def converte_para_leet(texto):
    texto_em_leet = ''
    for letra in texto:
        if(letra in alfabeto):
            letra = alfabeto[letra]
        texto_em_leet += letra
    return texto_em_leet

texto = input('Digite um texto: ').upper()
texto_em_leet = converte_para_leet(texto)
print(texto_em_leet)