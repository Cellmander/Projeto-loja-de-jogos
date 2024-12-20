class TelaUsuario():
    def opcoes_tela(self):
        while True:
            print("-------- Tela Usuario ----------")
            print("Escolha a opcao")
            print("1 - Cadastrar Usuário")
            print("2 - Alterar Usuário")
            print("3 - Excluir Usuário")
            print("4 - Adicionar Amigo")
            print("5 - Excluir Amigo")
            print("6 - Depositar Saldo")
            print("7 - Meus Jogos")
            print("8 - Meus amigos")
            print("9 - Verificar saldo")
            print("0 - Retornar")

            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao > 9 or opcao < 0:
                    raise ValueError
                return opcao
            except ValueError:
                self.mostra_mensagem("Entrada inválida! Por favor, insira um número correspondente à opção.")

    def dados_usuario(self):
        while True:
            try:
                print("-----DADOS USUÁRIO-----")
                nome = input("Nome: ")
                nickname = input("Nickname: ")
                idade = int(input("Idade: "))
                email = input("E-mail: ")
                endereco = input("Endereço: ")
                senha = input("Senha: ")
                cpf = input("CPF: ")
                return {"nome": nome, "nickname": nickname, "idade": idade, "email": email, "endereco": endereco, "senha": senha, "cpf": cpf}
            except ValueError:
                self.mostra_mensagem("Informação inválida, tente novamente!")


    def pede_nickname(self, nome):
        nickname = input(nome)
        return nickname

    def pede_senha(self):
        senha = input("Insira sua senha: ")
        return senha

    def valor_deposito(self):
        valor = float(input("Insira a quantia que deseja depositar: "))
        return valor

    def dados_alteracao(self):
        print("----- ALTERAR DADOS DO USUÁRIO -----")
        nome = input("Novo Nome (deixe em branco para manter o atual): ")
        nickname = input("Novo Nickname (deixe em branco para manter o atual): ")
        idade = input("Nova Idade (deixe em branco para manter a atual): ")
        email = input("Novo E-mail (deixe em branco para manter o atual): ")
        endereco = input("Novo Endereço (deixe em branco para manter o atual): ")
        senha = input("Nova Senha (deixe em branco para manter a atual): ")

        return {
            "nome": nome if nome else None,
            "nickname": nickname if nickname else None,
            "idade": int(idade) if idade else None,
            "email": email if email else None,
            "endereco": endereco if endereco else None,
            "senha": senha if senha else None
        }

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")
