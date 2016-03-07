from models import Bola

def main():
    bola_user = Bola()
    bola_user.marca = input('Forneça a marca: ')
    bola_user.circunferencia = eval(input('Forneça a circunferencia: '))
    bola_user.cor = input('Forneça a cor: ')

    print('ID: %d' % id(bola_user))
    print('Marca %s ' % bola_user.marca)
    print('Circunferencia %d ' % bola_user.circunferencia)
    print('Cor %s ' % bola_user.cor)


if __name__ == '__main__':
    main()
