class Pessoa(object):
    _nome = None
    _sexo = None

    def __init__(self, nome, sexo, idade):
        self._nome = nome
        self._sexo = sexo
        self._idade = idade

    @property
    def nome(self):
        return self._nome.lower()

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sexo(self):
        return self._sexo.upper()

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade


class Amigo(Pessoa):

    def __init__(self, nome, sexo, idade, dia_aniversario=0):
        super().__init__(nome, sexo, idade)
        self._dia_aniversario = dia_aniversario

    @property
    def dia_aniversario(self):
        return self._dia_aniversario

    @dia_aniversario.setter
    def dia_aniversario(self, dia_aniversario):
        self._dia_aniversario = dia_aniversario
