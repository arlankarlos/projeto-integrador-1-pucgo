import sqlite3


conexao = sqlite3.connect('chatbot.db')

cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(conexao, cursor):
    """
    Cria a tabela alunos no banco de dados se ela n o existir.

    :param conexao: conex o para o banco de dados
    :param cursor: cursor para o banco de dados
    """
    cursor.execute('CREATE TABLE IF NOT EXISTS alunos(id INTEGER PRIMARY KEY, nome VARCHAR(100), cpf VARCHAR(11), media INTEGER)')
    conexao.commit()


def inserir_registro(conexao, cursor, nome, cpf, media):
    """
    Insere um aluno no banco de dados.

    :param conexao: conex o para o banco de dados
    :param cursor: cursor para o banco de dados
    :param nome: nome do aluno
    :param cpf: cpf do aluno
    :param media: media do aluno
    """
    data = (nome, cpf, media)
    cursor.execute('INSERT INTO alunos (nome, cpf, media) VALUES (?, ?, ?);', data)
    conexao.commit()


def inserir_lista(conexao, cursor, lista):
    """
    Insere uma lista de alunos no banco de dados.

    :param conexao: conex o para o banco de dados
    :param cursor: cursor para o banco de dados
    :param lista: lista de tuplas, onde cada tupla representa um aluno
                  com nome, cpf e media, respectivamente
    """
    
    cursor.executemany('INSERT INTO alunos (nome, cpf, media) VALUES (?, ?, ?);', lista)
    conexao.commit()


def atualizar_registro(conexao, cursor, media, id):
    """
    Atualiza a media de um aluno com o id especificado no banco de dados.

    :param conexao: conex o para o banco de dados
    :param cursor: cursor para o banco de dados
    :param media: nova media do aluno
    :param id: id do aluno a ser atualizado
    """
    data = (media,id)
    cursor.execute('UPDATE alunos SET media = ? WHERE id = ?;', data)
    conexao.commit()


def deletar_registro(conexao, cursor, id):
    """
    Remove um aluno do banco de dados com o id especificado.

    :param conexao: conex o para o banco de dados
    :param cursor: cursor para o banco de dados
    :param id: id do aluno a ser removido
    """
    data = (id,)
    cursor.execute('DELETE FROM alunos WHERE id = ?;', data)
    conexao.commit()


def selecionar_aluno(cursor, id):
    """
    Retorna um aluno cadastrado no banco de dados com o id especificado.

    :param cursor: cursor para o banco de dados
    :param id: id do aluno a ser selecionado
    :return: um aluno, representado por um objeto Row
    """
    cursor.execute('SELECT * FROM alunos WHERE id = ?;', (id,))
    return cursor.fetchone()


def selecionar_todos_alunos(cursor):
    """
    Retorna uma lista de todos os alunos cadastrados no banco de dados, ordenados
    pelo nome em ordem decrescente.

    :param cursor: cursor para o banco de dados
    :type cursor: sqlite3.Cursor

    :return: lista de alunos
    :rtype: list
    """
    cursor.execute('SELECT * FROM alunos ORDER BY nome DESC;')
    return cursor.fetchall()

