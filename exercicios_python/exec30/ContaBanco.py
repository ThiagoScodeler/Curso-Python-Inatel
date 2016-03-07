class ContaBanco(object):
    nome_correntista = str()
    numero_da_conta = 0
    saldo = 0

    def __init__(self, nome_correntista, numero_da_conta, saldo=0):
        self.nome_correntista = nome_correntista
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo

    def alterarNome(self, novo_nome_correntista):
        self.nome_correntista = novo_nome_correntista

    def depositar(self, deposito):
        self.saldo += deposito

    def sacar(self, saque):
        self.saldo -= saque
