from Entidade.organizador import Organizador
from Entidade.participante import Participante


class Evento:
    def __init__(self, codigo: int, data: str, horario: str, local: str, capacidade: int, organizador: Organizador, participante: Participante, apresentar_comprovante: str):
        self.__codigo = codigo
        self.__data = data
        self.__horario = horario
        self.__local = local
        self.__capacidade = capacidade
        self.__organizador = []
        self.__organizador.append(organizador)
        self.__participante = []
        self.__participante.append(participante)
        self.__apresentar_comprovante = apresentar_comprovante

    @property
    def codigo(self):
        return self.__codigo

    @property
    def data(self):
        return self.__data

    @property
    def horario(self):
        return self.__horario

    @property
    def local(self):
        return self.__local

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def organizador(self):
        return self.__organizador

    @property
    def participante(self):
        return self.__participante

    @property
    def apresentar_comprovante(self):
        return self.__apresentar_comprovante

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @data.setter
    def data(self, data):
        self.__data = data

    @horario.setter
    def horario(self, horario):
        self.__horario = horario

    @local.setter
    def local(self, local):
        self.__local = local

    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @organizador.setter
    def organizador(self, organizador):
        self.organizador = organizador

    @participante.setter
    def participante(self, participante):
        self.__participante = participante

    @apresentar_comprovante.setter
    def apresentar_comprovante(self, apresentar_comprovante):
        self.__apresentar_comprovante = apresentar_comprovante