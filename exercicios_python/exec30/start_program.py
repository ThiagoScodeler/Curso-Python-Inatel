from ContaBanco import ContaBanco

def main():

    nome = input('Forneça o nome: ')
    numero_conta = eval(input('Forneça numero da conta: '))

    nova_conta = ContaBanco(nome,numero_conta)

    print('Menu do Banco')
    print('1 - Alterar nome')
    print('2 - Depositar')
    print('3 - Sacar')
    opcao = eval(input('Escolha uma opção\n'))

    if opcao == 1:
        novo_nome = input('Forneça o novo nome: ')
        nova_conta.alterarNome(novo_nome)
        print('Novo nome: %s' % nova_conta.nome_correntista)

    if opcao == 2:
        valor_deposito = eval(input('Valor do depósito: '))
        nova_conta.depositar(valor_deposito)
        print('Saldo com depósito realizado: %s' % nova_conta.saldo)

    if opcao == 3:
        valor_saque = eval(input('Valor do saque: '))
        nova_conta.sacar(valor_saque)
        print('Saldo com saque realizado: %s' % nova_conta.saldo)

    print('Saldo atual %d' % nova_conta.saldo)

if __name__ == '__main__':
    main()
