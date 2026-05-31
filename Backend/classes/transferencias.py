import sqlite3
from rich.console import Console
from rich.table import Table

from utils.validacao import validar_numero_float, validar_senha


class Transferencias:
    def __init__(self, id):
        self.__id = id

    def realizar_deposito(self):
        valor = validar_numero_float(input('Digite o valor do deposito: '))
        conexao = sqlite3.connect('database/dados.db')
        cursor = conexao.cursor()
        cursor.execute('''SELECT saldo FROM conta WHERE id_usuario = ?''', self.__id)
        saldo = cursor.fetchone()[0]
        saldo += abs(valor)
        cursor.execute('''UPDATE conta SET saldo = ? WHERE id_usuario = ?''', (saldo, self.__id))
        cursor.execute('INSERT INTO transferencia (valor,tipo_de_transferencia,id_usuario) VALUES (?,?,?)', (valor,'Deposito', self.__id))

        if cursor.rowcount > 0:
            print('deposito realizado com sucesso')
        else:
            print('Falha ao realizar deposito, tente novamente mais tarde')
        conexao.commit()
        conexao.close()

    def realizar_saque(self):
        valor = abs(validar_numero_float(input('Digite o valor do saque: ')))
        validar = validar_senha(self.__id, input('Digite sua senha: ').strip())
        if validar == 'INCORRETO':
            return ('INCORRETO')
        else:
            conexao = sqlite3.connect('database/dados.db')
            cursor = conexao.cursor()
            cursor.execute("""SELECT saldo FROM conta WHERE id_usuario = ?""", self.__id)
            saldo = cursor.fetchone()[0]
            if saldo < valor:
                print('Saldo insuficiente')
            else:
                saldo -= valor
                cursor.execute('UPDATE conta SET saldo = ? WHERE id_usuario = ?', (saldo, self.__id))
                cursor.execute('INSERT INTO transferencia (valor,tipo_de_transferencia,id_usuario) VALUES (?,?,?)',
                               (valor, 'Saque', self.__id))
                if cursor.rowcount > 0:
                    print('Saque realizado com sucesso')
                else:
                    print('Falha ao realizar saque')
            conexao.commit()
            conexao.close()

    def realizar_transferencia(self):
        valor = abs(validar_numero_float(input('Digite o valor do transferencia: ')))
        validar = validar_senha(self.__id, input('Digite sua senha: ').strip())
        if validar == 'INCORRETO':
            return ('INCORRETO')
        else:
            conexao = sqlite3.connect('database/dados.db')
            cursor = conexao.cursor()

            cursor.execute("""SELECT saldo FROM conta WHERE id_usuario = ?""", self.__id)
            saldo = cursor.fetchone()[0]
            if valor > saldo:
                print('Saldo insuficiente')
            else:
                try:
                    id_para_transferencia = input('Digite o id do usuario para transferencia: ')
                    cursor.execute("""SELECT saldo FROM conta WHERE id_usuario = ?""", id_para_transferencia)
                    saldo_para_transferencia = cursor.fetchone()[0]
                except:
                    print('Erro ao encontrar id para transferencia')
                else:
                    saldo_para_transferencia += valor
                    cursor.execute("""UPDATE conta SET saldo = ? WHERE id_usuario = ?""", (saldo_para_transferencia, id_para_transferencia))
                    if cursor.rowcount > 0:
                        cursor.execute("""INSERT INTO transferencia (valor, tipo_de_transferencia,id_usuario) VALUES (?,?,?)""", (valor, 'Transferencia_recebe', id_para_transferencia))
                        saldo -= valor
                        cursor.execute("""UPDATE conta SET saldo = ? WHERE id_usuario = ?""", (saldo,self.__id))
                        if cursor.rowcount > 0:
                            cursor.execute("""INSERT INTO transferencia (valor, tipo_de_transferencia,id_usuario) VALUES (?,?,?)""", (valor, 'Transferencia_envia', self.__id))
                            print('Transferencia realizada com sucesso')
                            conexao.commit()
                        else:
                            print('Falha ao realizar transferencia')
                    else:
                        print('Falha ao realizar transferencia')
                    conexao.close()

    def verificar_transferencia(self):
        conexao = sqlite3.connect('database/dados.db')
        cursor = conexao.cursor()

        tabela = Table()
        tabela.add_column('id', justify='center')
        tabela.add_column('Valor', justify='center')
        tabela.add_column('Tipo de transferência', justify='left')

        cursor.execute("""SELECT id, valor, tipo_de_transferencia FROM transferencia WHERE id_usuario = ?""", self.__id)
        for transferencia in cursor.fetchall():
            id, valor, tipo_de_transferencia = transferencia
            tabela.add_row(f'{id}', f'{valor}', f'{tipo_de_transferencia}')

        conexao.close()
        console = Console()
        console.print(tabela)

