
class Interface:

    def linha(self):
        print('-'*30)

    def cabecalho(self, titulo):
        self.linha()
        print(f'[green]{titulo: ^30}[/green]')
        self.linha()

    def menu_principal(self):
        self.cabecalho('Menu principal')
        print('''1 - Criar novo usuario
2 - Ver lista de usuarios
3 - Acessar conta
4 - encerrar programa''')
        self.linha()

    def menu_do_usuario(self):
        self.cabecalho('Menu do usuario')
        print('''1 - Verificar saldo da conta
2 - Realizar depósito
3 - Realizar saque
4 - Realizar transferencia
5 - Mudar senha
6 - Encerrar seção
7 - Excluir conta''')
        self.linha()
