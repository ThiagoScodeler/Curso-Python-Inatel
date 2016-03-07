class Time(object):

    def __init__(self, nome, tecnico):
        self.nome = nome
        self.tecnico = tecnico
        self.atletas = []

    def add_atleta(self,atleta):
        self.atletas.append(atleta)


class Atleta(object):

    def __init__(self, nome, idade, posicao):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
