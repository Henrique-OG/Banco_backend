from database.tabelas import *
from utils.interface import *
from utils.validacao import validar_escolha, validar_numero_inteiro

while True:
    menu_do_usuario()
    escolha_do_usuario = validar_numero_inteiro(input('Digite sua escolha: '))
    validar_escolha(escolha_do_usuario, 7)