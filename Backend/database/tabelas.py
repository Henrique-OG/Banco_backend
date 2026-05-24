import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('database/dados.db')
    cursor = conexao.cursor()

    criar_tabela_de_usuarios = """CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
    )"""

    criar_tabela_da_conta = """CREATE TABLE IF NOT EXISTS conta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    saldo FLOAT NOT NULL,
    id_usuario INTEGER NOT NULL,
    
    FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE
    )"""

    criar_tabela_de_transferencias = """CREATE TABLE IF NOT EXISTS transferencia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor FLOAT NOT NULL,
    tipo_de_transferencia TEXT NOT NULL,
    id_usuario INTEGER NOT NULL,
    
    FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE
    )"""

    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute(criar_tabela_de_usuarios)
    cursor.execute(criar_tabela_da_conta)
    cursor.execute(criar_tabela_de_transferencias)

    conexao.commit()
    conexao.close()

