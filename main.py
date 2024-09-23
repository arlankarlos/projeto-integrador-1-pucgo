# Projeto Chat Bot
from banco_de_respostas import principal, fundo1
from uteis import *
from sqlite_util import *


while chave_externa:

    menu()
    chave_interna = True
    entrada = input("Selecione uma opção: ")
    if entrada == "1":
        while chave_interna:
            menu_escolhido(entrada)
            chave_interna = escolha(entrada)
            chave_interna

            # for key, value in banco_de_respostas.items():
            #     print(f'{key}: {value[0]}')
    elif entrada == "2":
        pass
    elif entrada == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")




# dados = [
#     ('Joaquim', '12345678910', 4),
#     ('Bruna', '12345678910', 5),
#     ('Lucas', '12345678910', 3),
#     ('Pedro', '12345678910', 2),
#     ('Carlos', '12345678910', 1),
#     ('Lucas', '12345678910', 4),

# ]
# Comandos executados uma única vez
# criar_tabela(conexao, cursor)
# inserir_lista(conexao, cursor, dados)
# atualizar_registro(conexao, cursor, 10, 1)
# alunos = selecionar_todos_alunos(cursor)
# for aluno in alunos:
#     print(aluno['id'], aluno['nome'], aluno['cpf'], aluno['media'])




    # print(f'Bot: \t{banco_de_respostas[entrada][0]}')
    # for resposta in range(1, len(banco_de_respostas[entrada])):
    #     print(f'\t {resposta}: {banco_de_respostas[entrada][resposta]}')

    # back_entrada = entrada
    # back_resposta = resposta

    # while True:
    #     entrada = input("Você: ")
    #     if entrada.isnumeric():
    #         entrada = int(entrada)
    #         if (entrada <= len(banco_de_respostas[back_entrada])-1) and (entrada > 0):
    #             break

    # print(banco_de_respostas[back_entrada][entrada])
    # if entrada == len(banco_de_respostas[back_entrada])-1:
    #     if banco_de_respostas[back_entrada][4] == 'Encerrar.':
    #         break
    #     else:
    #         entrada = 'inicio'
