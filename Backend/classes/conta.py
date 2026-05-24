import sqlite3
from utils.validacao import *
from rich.table import Table
from rich.console import Console
from utils.interface import *

class Banco:

    def criar_conta(self):
        conexao = sqlite3.connect('database/dados.db')
        cursor = conexao.cursor()

        nome = input('Digite seu nome: ').strip().title()
        email = validar_email(input('Digite seu email: ').strip().lower())
        senha = criptografar_senha(input('Digite sua senha: '))

        try:
            cursor.execute('''INSERT INTO usuario (nome, email, senha) VALUES (?, ?, ?)''', (nome, email, senha))
            cursor.execute('INSERT INTO conta (saldo,id_usuario) VALUES (0, ?)',(cursor.lastrowid,))
            conexao.commit()
            conexao.close()
            print('Conta criada com sucesso!')
        except sqlite3.IntegrityError:
            print('Erro ao criar conta, veriifique se o email já foi registrado anteriormente')

    def ver_lista_de_usuarios(self):

        conexao = sqlite3.connect('database/dados.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT id,nome,email FROM usuario')
        usuarios = cursor.fetchall()

        linha()

        tabela = Table(title='Usuarios')
        tabela.add_column('id', justify='center')
        tabela.add_column('Nome', justify='center')
        tabela.add_column('Email', justify='center')

        for users in usuarios:
            tabela.add_row(f'{users[0]}', f'{users[1]}', f'{users[2]}')

        console = Console()
        console.print(tabela)
        conexao.close()