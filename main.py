# Projeto Chat Bot
from uteis import *


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
