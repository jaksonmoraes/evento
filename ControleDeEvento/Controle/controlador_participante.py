from Limite.tela_participante import TelaParticipante
from Entidade.participante import Participante

class ControlaParticipante:
    def __init__(self, controla_sistema):
        self.__participante = []
        self.__tela_participante = TelaParticipante()
        self.__controlador_sistema = controla_sistema

    def busca_participante_por_cpf(self, cpf: int):
        for participante in self.__participante:
            if(participante.cpf == cpf):
                return participante
        return None

    def incluir_participante(self):
        dados_participante = self.__tela_participante.pega_dados_participante()
        participante = Participante(dados_participante["cpf"],
                        dados_participante["idade"],
                        dados_participante["nome"],
                        dados_participante["data_nascimento"],
                        dados_participante["endereco"])
        self.__participante.append(participante)

    def alterar_participante(self):
        self.listar_participante()
        cpf_participante = self.__tela_participante.selecionar_participante()
        participante = self.busca_participante_por_cpf(cpf_participante)

        if(participante is not None):
            novos_dados_participante = self.__tela_participante.pega_dados_participante()
            participante.nome = novos_dados_participante["nome"]
            participante.nome = novos_dados_participante["cpf"]
            participante.nome = novos_dados_participante["idade"]
            participante.nome = novos_dados_participante["data_nascimento"]
            participante.nome = novos_dados_participante["endereco"]
            self.listar_participante()
        else:
            self.__tela_participante.mostra_mensagem("Nao foi encontrado este participante")

    # mostrar lista vazia se não houver pessoas
    def listar_participante(self):
        for participante in self.__participante:
            self.__tela_participante.mostrar_participante({"nome": participante.nome,
                                                  "cpf": participante.cpf,
                                                  "idade": participante.idade,
                                                  "data_nascimento": participante.data_nascimento,
                                                  "endereco": participante.endereco})

    def excluir_participante(self):
        self.listar_participante()
        cpf_pessoa = self.__tela_participante.selecionar_participante()
        pessoa = self.busca_participante_por_cpf(cpf_pessoa)

        if(pessoa is not None):
            self.__participante.remove(pessoa)
            self.listar_participante()
        else:
            self.__tela_participante.mostra_mensagem("Pessoa inexistente")

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.incluir_participante,
                        2: self.alterar_participante,
                        3: self.listar_participante,
                        4: self.excluir_participante,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_participante.tela_opcoes()]()