from stdiomask import getpass
from hashlib import sha256
import sqlite3


def validar_numero_inteiro(numero):
    numero = str(numero)
    while numero.isnumeric() == False:
        print('NUMERO INVALIDO')
        numero = input('Digite um valor valido: ')
    return int(numero)

def validar_escolha(escolha, quantidade):
    escolha = validar_numero_inteiro(escolha)
    while escolha not in range(1, quantidade + 1):
        print('Opção invalida')
        escolha = validar_numero_inteiro(input('Digite um valor valido: '))
    return escolha

def criptografar_senha(senha):
    senha = str(senha)
    senha = sha256(senha.encode()).hexdigest()
    return senha

def validar_email(email):
    while '@gmail.com' not in email:
        email = input('Digite um email valido: ')
    return email

def validar_senha(id,senha):
    conexao = sqlite3.connect('database/dados.db')
    cursor = conexao.cursor()

    senha = criptografar_senha(senha)

    cursor.execute('''SELECT senha FROM usuario WHERE id = ?''', (id,))
    senha_original = cursor.fetchone()

    print(senha_original[0])
    print(senha)

    if senha == senha_original[0]:
        print('Senha valida!')
    else :
        print('Senha invalida!')