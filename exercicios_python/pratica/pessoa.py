class Pessoa(object):
    nome = str()
    idade = 0
    peso = 0
    altura = 0

    def __init__(self, nome, idade, altura, peso=0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def engordar(self, novo_peso):
        self.peso += novo_peso

    def emagrecer(self):
        self.peso -= 1

    def crescer(self):
        self.altura += 0.5

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5

if __name__ == '__main__':
    pessoa = Pessoa('thiago',25,1.8)

    pessoa.engordar(8)
    print('Peso %d' % pessoa.peso)

    for i in range(18):
        pessoa.envelhecer()

    print('Idade %d' % pessoa.idade)
    print('Altura %d' % pessoa.altura)
