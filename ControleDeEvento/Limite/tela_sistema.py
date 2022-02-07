class TelaSistema:
    # tratar as exceções aqui
    def tela_opcoes(self):
        print("-------- Controle de Vacinacao --------")
        print("Escolha sua opcao")
        print("1 - Participante")
        print("2 - Organizador")
        print("3 - Evento")

        print("0 - Encerrar sistema")

        opcao = int(input("Escolha a opcao\n\n"))
        return opcao