from classes.conta import *
from classes.transferencias import Transferencias
from classes.usuario import Usuario
from database.tabelas import *
from utils.interface import *
from utils.validacao import *
from classes.conta import *
from time import sleep

criar_tabela()
banco = Banco()

while True:
    sleep(0.5)
    menu_principal()
    escolha_do_usuario = validar_escolha(input('Digite sua escolha: '), 4)

    if escolha_do_usuario == 1:
        sleep(0.5)
        banco.criar_conta()
    elif escolha_do_usuario == 2:
        banco.ver_lista_de_usuarios()
        sleep(0.5)
    elif escolha_do_usuario == 4:
        sleep(0.5)
        break
    elif escolha_do_usuario == 3:
        sleep(0.5)
        id = input('Digite o ID da conta: ')
        acesso = banco.acessar_conta(id)
        if acesso == 'CORRETO':
            usuario = Usuario(id)
            transferencais = Transferencias(id)
            while True:
                menu_do_usuario()
                escolha_do_usuario = validar_escolha(input('Digite sua escolha: '), 8)
                if escolha_do_usuario == 1:
                    sleep(0.5)
                    usuario.verificar_saldo()
                elif escolha_do_usuario == 2:
                    transferencais.realizar_deposito()
                elif escolha_do_usuario == 3:
                    validar = transferencais.realizar_saque()
                    if validar == 'INCORRETO':
                        break
                elif escolha_do_usuario == 4:
                    validar = transferencais.realizar_transferencia()
                    if validar == 'INCORRETO':
                        break
                elif escolha_do_usuario == 5:
                    transferencais.verificar_transferencia()
                    sleep(2)
                elif escolha_do_usuario == 6:
                    sleep(0.5)
                    validar_seguranca = usuario.mudar_senha()
                    if validar_seguranca == 'INCORRETO':
                        break
                elif escolha_do_usuario == 8:
                    sleep(0.5)
                    usuario.excluir_conta()
                    break
                elif escolha_do_usuario == 7:
                    break


print('Programa finalizado com sucesso!')
