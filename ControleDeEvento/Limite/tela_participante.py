class TelaParticipante:
    # tratar as exceções aqui
    def numero_inteiro(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int (valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto, digite novamente")
                if inteiros_validos:
                    print("Valores validos: ", inteiros_validos)
    def tela_opcoes(self):
        print("-------- Participantes do evento --------")
        print("Escolha a opcao\n")
        print("1 - Cadastrar Participante")
        print("2 - Alterar Participante")
        print("3 - Listar Participante")
        print("4 - Excluir Participante")
        print("0 - Retornar")

        opcao = self.numero_inteiro("Escolha a opcao\n", [1, 2, 3, 4, 0])
        #opcao = int(input("Escolha a opcao"))
        return opcao

    # tratar as exceções
    def pega_dados_participante(self):
        print("------Informe os dados do participanteeee------")
        nome = input("Nome: ")
        cpf = self.numero_inteiro(("CPF: "))
        idade = input("Idade: ")
        data_nascimento = input("Data de Nascimento: ")
        endereco = input("Endereco: ")
        return {"nome": nome,
                "cpf": cpf,
                "idade": idade,
                "data_nascimento": data_nascimento,
                "endereco": endereco}

    # tratar as exceções
    def mostrar_participante(self, dados_participante):
         print("Nome do participante: ", dados_participante)
         print("CPF: ", dados_participante)
         print("Idade: ", dados_participante)
         print("Data de nascimento: ", dados_participante)
         print("Endereco: ", dados_participante)

    #tratar exceções
    def selecionar_participante(self):
         cpf = input("Digite o CPF: ")
         return cpf

    def mostra_mensagem(self, msg):
        print(msg)