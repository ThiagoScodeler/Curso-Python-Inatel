from entidades import Time, Atleta

def main():

    atleta = Atleta('zoio',40,'goleiro')
    time = Time('Corithians','Tite')
    print('Total de atletas %d do time: %s' % (len(time.atletas),time.nome))

    time.add_atleta(atleta)
    print('Total de atletas %d do time: %s' % (len(time.atletas),time.nome))

if __name__ == '__main__':
    main()
