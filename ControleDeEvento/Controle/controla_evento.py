from Limite.tela_evento import TelaEvento
from Entidade.evento import Evento
from Controle.controlador_participante import ControlaParticipante


class ControlaEvento:
    def __init__(self, controla_evento):
        self.__evento = []
        self.__tela_evento = TelaEvento()
        self.__controlador_evento = controla_evento

    def busca_evento_por_codigo(self, codigo: int):
        for evento in self.__evento:
            if (evento.codigo == codigo):
                return evento
        return None

    def incluir_evento(self):
        dados_evento = self.__tela_evento.pega_dados_evento()
        evento = Evento(dados_evento["codigo"],
                        dados_evento["data"],
                        dados_evento["horario"],
                        dados_evento["local"],
                        dados_evento["capacidade"],
                        dados_evento["organizador"],
                        dados_evento["participante"],
                        dados_evento["apresentar_comprovante"])
        self.__evento.append(evento)
        print(ControlaParticipante.listar_participante(self))

    def alterar_evento(self):
        self.listar_evento()
        codigo_evento = self.__tela_evento.selecionar_evento()
        evento = self.busca_evento_por_codigo(codigo_evento)

        if(evento is not None):
            novos_dados_evento = self.__tela_evento.pega_dados_evento()
            evento.codigo = novos_dados_evento["codigo"]
            evento.data = novos_dados_evento["data"]
            evento.horario = novos_dados_evento["horario"]
            evento.local = novos_dados_evento["local"]
            evento.capacidade = novos_dados_evento["capacidade"]
            evento.organizador = novos_dados_evento["organizador"]
            evento.participante = novos_dados_evento["participante"]
            evento.apresentar_comprovante = novos_dados_evento["apresentar_comprovante"]
            self.listar_evento()
        else:
            self.__tela_evento.mostra_mensagem("Nao foi encontrado este evento")

    # mostrar lista vazia se não houver organizadores
    def listar_evento(self):
        for evento in self.__evento:
            self.__tela_evento.mostrar_evento({"codigo": evento.codigo,
                                                "data":  evento.data,
                                                "horario": evento.horario,
                                                "local": evento.local,
                                                "capacidade": evento.capacidade,
                                                "organizador": evento.organizador,
                                                "participante": evento.participante,
                                                "apresentar-comprovante": evento.apresentar_comprovante})

    def excluir_evento(self):
        self.listar_evento()
        codigo_evento = self.__tela_evento.selecionar_evento()
        evento = self.busca_evento_por_codigo(codigo_evento)

        if(evento is not None):
            self.__evento.remove(evento)
            self.listar_evento()
        else:
            self.__tela_evento.mostra_mensagem("Evento inexistente")

    def retornar(self):
        self.__controlador_evento.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.incluir_evento,
                        2: self.alterar_evento,
                        3: self.listar_evento,
                        4: self.excluir_evento,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_evento.tela_opcoes()]()