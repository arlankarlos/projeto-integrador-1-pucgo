# Projeto Integrador - Chat Bot
# Instituição: Pontifícia Universidade Católica de Goiás - PUC-GO
# Curso: Big Data e Inteligência Artificial
# Professor: Carlos Henrique Rorato Souza 
# Disciplina: Projeto Integrador I-A
# Aluno: Arlan Karlos Gouveia do Nascimento
"""
bibliotecas: 
unidecode ### $ pip install unidecode
dotenv ### $ pip install python-dotenv
"""
from uteis import *

def main() -> None:

    while chave_externa:

        menu()
        chave_interna = True
        entrada = input("Selecione uma opção: ")
        if entrada == "1":
            while chave_interna:
                menu_escolhido(entrada)
                chave_interna = escolha(entrada)
                chave_interna

        elif entrada == "2":
            while chave_interna:
                menu_escolhido(entrada)
                chave_interna = escolha(entrada)
                chave_interna
        elif entrada == "3":
            print("Bot: Sou o assistente virtual da PUC-GO.\nBot: Digite 'sair' para encerrar o programa.\n")
            nome_usuario = input("Qual o seu nome? ")
            while True:
                pergunta = clean_input(nome_usuario)
                if pergunta == "sair":
                    break
                responder(pergunta, nome_usuario)


        elif entrada == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
