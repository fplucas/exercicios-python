from decimal import Decimal

class Conta_corrente():
    def __init__(self, numero_da_conta, nome_do_correntista, saldo = Decimal('0')):
        self.numero_da_conta = numero_da_conta
        self.nome_do_correntista = nome_do_correntista
        self.saldo = saldo

    def altera_nome(self, nome):
        self.nome_do_correntista = nome

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor