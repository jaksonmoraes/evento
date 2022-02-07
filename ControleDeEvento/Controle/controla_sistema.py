from Limite.tela_sistema import TelaSistema
from Controle.controlador_participante import ControlaParticipante
from Controle.controlador_organizador import ControlaOrganizador
from Controle.controla_evento import ControlaEvento

class ControladorSistema:
    def __init__(self):
        self.__controlador_participante = ControlaParticipante(self)
        self.__controla_organizador = ControlaOrganizador(self)
        self.__controla_evento = ControlaEvento(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controla_participante(self):
        return self.__controlador_participante

    @property
    def controla_organizador(self):
        return self.__controla_organizador

    @property
    def controla_evento(self):
        return self.__controla_evento

    def inicializar_sistema(self):
        self.abrir_tela()

    def cadastrar_participante(self):
        self.__controlador_participante.abrir_tela()

    def cadastrar_organizador(self):
        self.__controla_organizador.abrir_tela()

    def cadastrar_evento(self):
        self.__controla_evento.abrir_tela()

    def encerrar_sistema(self):
        exit(0)

    def abrir_tela(self):
        listar_opcoes = {
            1: self.cadastrar_participante, 2: self.cadastrar_organizador, 3: self.cadastrar_evento, 0: self.encerrar_sistema
        }
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = listar_opcoes[opcao_escolhida]
            funcao_escolhida()
