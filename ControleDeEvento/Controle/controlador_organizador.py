from Limite.tela_organizador import TelaOrganizador
from Entidade.organizador import Organizador


class ControlaOrganizador:
    def __init__(self, controla_sistema):
        self.__organizador = []
        self.__tela_organizador = TelaOrganizador()
        self.__controlador_sistema = controla_sistema

    def busca_organizador_por_cpf(self, cpf: int):
        for organizador in self.__organizador:
            if(organizador.cpf == cpf):
                return organizador
        return None

    def incluir_organizador(self):
        dados_organizador = self.__tela_organizador.pega_dados_organizador()
        organizador = Organizador(dados_organizador["cpf"],
                        dados_organizador["idade"],
                        dados_organizador["nome"],
                        dados_organizador["data_nascimento"],
                        dados_organizador["endereco"])
        self.__organizador.append(organizador)

    def alterar_organizador(self):
        self.listar_organizador()
        cpf_organizador = self.__tela_organizador.selecionar_organizador()
        organizador = self.busca_organizador_por_cpf(cpf_organizador)

        if(organizador is not None):
            novos_dados_organizador = self.__tela_organizador.pega_dados_organizador()
            organizador.nome = novos_dados_organizador["nome"]
            organizador.cpf = novos_dados_organizador["cpf"]
            organizador.idade = novos_dados_organizador["idade"]
            organizador.data_nascimento = novos_dados_organizador["data_nascimento"]
            organizador.endereco = novos_dados_organizador["endereco"]
            self.listar_organizador()
        else:
            self.__tela_organizador.mostra_mensagem("Nao foi encontrado este organizador")

    # mostrar lista vazia se não houver organizadores
    def listar_organizador(self):
        for organizador in self.__organizador:
            self.__tela_organizador.mostrar_organizador({"nome": organizador.nome,
                                                  "cpf":  organizador.cpf,
                                                  "idade": organizador.idade,
                                                  "data_nascimento": organizador.data_nascimento,
                                                  "endereco": organizador.endereco})

    def excluir_organizador(self):
        self.listar_organizador()
        cpf_organizador = self.__tela_organizador.selecionar_organizador()
        organizador = self.busca_organizador_por_cpf(cpf_organizador)

        if(organizador is not None):
            self.__organizador.remove(organizador)
            self.listar_organizador()
        else:
            self.__tela_organizador.mostra_mensagem("Organizador inexistente")

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.incluir_organizador,
                        2: self.alterar_organizador,
                        3: self.listar_organizador,
                        4: self.excluir_organizador,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_organizador.tela_opcoes()]()