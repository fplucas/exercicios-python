from decimal import Decimal

class Produto():
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco

cachorro_quente = Produto('Cachorro Quente', Decimal('1.2'))
bauru_simples = Produto('Bauru Simples', Decimal('1.3'))
bauru_com_ovo = Produto('Bauru com ovo', Decimal('1.5'))
hamburguer = Produto('Hambúrguer', Decimal('1.2'))
cheeseburguer = Produto('Cheeseburguer', Decimal('1.3'))
refrigerante = Produto('Refrigerante', Decimal('1'))
cardapio = {100: cachorro_quente, 101: bauru_simples, 102: bauru_com_ovo, 103: hamburguer, 104: cheeseburguer, 105: refrigerante}

class Item():
    def __init__(self, Produto, quantidade):
        self.Produto = Produto
        self.quantidade = quantidade

    def calcula_preco(self, quantidade):
        preco = self.Produto.preco * quantidade
        return preco

print('''Cardápio
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00''')
cupom = []
venda = True
while(venda):
    codigo = 0
    while(codigo not in cardapio):
        codigo = int(input('Entre com o código do item. 0 - Finaliza venda: '))
        if(codigo in cardapio):
            produto = cardapio[codigo]
        else:
            print('Favor entrar com um código válido!')
    quantidade = int(input('Quantidade: '))
    item = Item(produto, quantidade)
    cupom.append(item)
    continua = input(
        'Deseja continuar a compra? Enter para continuar / N para finalizar. ')
    if(continua.upper() == 'N'):
        venda = False

print('Produto: Quantidade x Preço unitário = Preço total')
soma = 0
for item in cupom:
    preco_total = item.calcula_preco(quantidade)
    print('{}: {} x {} = {}'.format(item.Produto.descricao, item.quantidade, item.Produto.preco, preco_total))
    soma += preco_total

print('Valor total da compra: {}'.format(soma))