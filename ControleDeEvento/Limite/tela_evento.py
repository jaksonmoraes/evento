class TelaEvento:
    # tratar as exceções aqui
    def tela_opcoes(self):
        print("-------- Dados de evento --------")
        print("Escolha a opcao\n")
        print("1 - Cadastrar evento")
        print("2 - Alterar evento")
        print("3 - Listar evento")
        print("4 - Excluir evento")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao\n"))
        return opcao

    # tratar as exceções
    def pega_dados_evento(self):
        print("------Dados evento------")
        codigo = input("Codigo: ")
        data = input("Data: ")
        horario = input("Horario: ")
        local = input("Local: ")
        capacidade = input("Capacidade: ")
        organizador = input("Organizador: ")
        participante = input("Participante: ")
        apresentar_comprovante = input("Apresentar Comprovante: ")
        return {"codigo": codigo,
                "data": data,
                "horario": horario,
                "local": local,
                "capacidade": capacidade,
                "organizador": organizador,
                "participante": participante,
                "apresentar_comprovante": apresentar_comprovante}

    # tratar as exceções
    def mostrar_evento(self, dados_evento):
         print("Codigo do envento: ", dados_evento)
         print("Data: ", dados_evento)
         print("Horario: ", dados_evento)
         print("Local: ", dados_evento)
         print("Capacidade: ", dados_evento)
         print("Organizador: ", dados_evento)
         print("Participante: ", dados_evento)
         print("Apresentar Comprovante: ", dados_evento)

    #tratar exceções
    def selecionar_evento(self):
         codigo = input("Digite o codigo do evento: ")
         return codigo

    def mostra_mensagem(self, msg):
        print(msg)