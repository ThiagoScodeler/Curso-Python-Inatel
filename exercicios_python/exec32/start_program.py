from entidades import Pessoa
from entidades import Amigo

def main():

    amigo = Amigo('Thiago','masculino',25)

    amigo.dia_aniversario = 8

    print(amigo.nome)
    print(amigo.sexo)
    print(amigo.idade)
    print(amigo.dia_aniversario)

if __name__ == '__main__':
    main()
