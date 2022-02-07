from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, cpf:int, idade:int, nome:str, data_nascimento:str, endereco:str):
        self.__cpf = cpf
        self.__idade = idade
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf

    @property
    def idade(self):
        return self.__idade

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def endereco(self):
        return self.__endereco

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
