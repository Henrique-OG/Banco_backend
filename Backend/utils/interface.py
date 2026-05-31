from rich import print

def linha():
    print('-'*30)

def cabecalho(titulo):
    linha()
    print(f'[green]{titulo: ^30}[/green]')
    linha()

def menu_principal():
    cabecalho('Menu principal')
    print('''1 - Criar novo usuario
2 - Ver lista de usuarios
3 - Acessar conta
4 - encerrar programa''')
    linha()

def menu_do_usuario():
    cabecalho('Menu do usuario')
    print('''1 - Verificar saldo da conta
2 - Realizar depósito
3 - Realizar saque
4 - Realizar transferencia
5 - Verificar hitórico de \n    transferencia
6 - Mudar senha
7 - Encerrar seção
8 - Excluir conta''')
    linha()
