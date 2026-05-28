from classes.conta import *
from database.tabelas import *
from utils.interface import *
from utils.validacao import *
from classes.conta import *

criar_tabela()
banco = Banco()

while True:
    menu_principal()
    escolha_do_usuario = validar_escolha(input('Digite sua escolha: '), 7)

    if escolha_do_usuario == 1:
        banco.criar_conta()
    elif escolha_do_usuario == 2:
        banco.ver_lista_de_usuarios()
    elif escolha_do_usuario == 3:
        banco.acessar_conta(input('Digite o ID da conta: '))
    elif escolha_do_usuario == 4:
        break

print('Programa finalizado com sucesso!')