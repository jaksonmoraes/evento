class TelaOrganizador:
    # tratar as exceções aqui
    def tela_opcoes(self):
        print("-------- Organizador do evento --------")
        print("Escolha a opcao\n")
        print("1 - Cadastrar organizador")
        print("2 - Alterar organizador")
        print("3 - Listar organizador")
        print("4 - Excluir organizador")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao\n"))
        return opcao

    # tratar as exceções
    def pega_dados_organizador(self):
        print("------Dados Organizador------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        idade = input("Idade: ")
        data_nascimento = input("Data de Nascimento: ")
        endereco = input("Endereco: ")
        return {"nome": nome,
                "cpf": cpf,
                "idade": idade,
                "data_nascimento": data_nascimento,
                "endereco": endereco}

    # tratar as exceções
    def mostrar_organizador(self, dados_organizador):
         print("Nome do participante: ", dados_organizador)
         print("CPF: ", dados_organizador)
         print("Idade: ", dados_organizador)
         print("Data de nascimento: ", dados_organizador)
         print("Endereco: ", dados_organizador)

    #tratar exceções
    def selecionar_organizador(self):
         cpf = input("Digite o CPF: ")
         return cpf

    def mostra_mensagem(self, msg):
        print(msg)