import sqlite3

from utils.interface import linha
from utils.validacao import validar_senha, criptografar_senha


class Usuario:
    def __init__(self, id):
        self.__id = id

    def verificar_saldo(self):
        conexao = sqlite3.connect('database/dados.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT saldo FROM conta WHERE id_usuario = ?', (self.__id,))
        saldo = cursor.fetchone()[0]
        print(f'Saldo na conta: {saldo}')

        conexao.close()

    def mudar_senha(self):

        print('Para mudar a senha, precisamos confirmar se é você')
        senha = input('Digite sua senha: ')
        entrada = validar_senha(self.__id, senha)
        if entrada == 'INCORRETO':
            return 'INCORRETO'
        elif entrada == 'CORRETO':
            linha()
            nova_senha = input('Digite sua nova senha: ')
            nova_senha = criptografar_senha(nova_senha)
            conexao = sqlite3.connect('database/dados.db')
            cursor = conexao.cursor()
            cursor.execute('UPDATE usuario SET senha = ? WHERE id = ?', (nova_senha, self.__id))

            conexao.commit()
            conexao.close()

            if cursor.rowcount > 0:
                print('Senha alterada com sucesso')
            else:
                print('Falha ao mudar senha')

    def excluir_conta(self):
        conexao = sqlite3.connect('database/dados.db')
        cursor = conexao.cursor()

        senha = input('Digite sua senha para confirmar solicitação: ')
        confiramar = validar_senha(self.__id, senha)
        if confiramar == 'CORRETO':
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute('DELETE FROM usuario WHERE id = ?', (self.__id,))
            conexao.commit()
            conexao.close()

            if cursor.rowcount > 0:
                print('Conta excluida com sucesso')
            else:
                print('Falha ao excluir conta, tente novamente mais tarde')
        else:
            print('Falha ao excluir conta')

