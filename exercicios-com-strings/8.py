def eh_palindromo(texto):
    if(texto == texto[::-1]):
        print('O texto informado é palíndromo!')
    else:
        print('O texto informado não é palíndromo!')

texto = input('Entre com o texto: ').replace(' ', '')
eh_palindromo(texto)