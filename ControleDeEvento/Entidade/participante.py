from Entidade.pessoa import Pessoa


class Participante(Pessoa):

    def __init__(self, cpf: int, idade: int, nome: str, data_nascimento: str, endereco: str):
        super().__init__(cpf, idade, nome, data_nascimento, endereco)
