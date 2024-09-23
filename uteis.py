from banco_de_respostas import principal, fundo1, fundo2
import random
import string
from unidecode import unidecode
# chaves para controle do while
chave_interna = True
chave_externa = True

def menu():
    menu = """\n\n\n\n\n
Bot:    Você é aluno da PUC-GO?

        1: Sim, sou PUC-GO.
        2: Ainda não sou PUC-GO, mas quero muito de ser!
        3: Oi bot. Quem é você?
        4: Encerrar.
    """
    print(menu)

def menu_escolhido(seletor):
    try:
        seletor = int(seletor)
        if seletor not in principal:
            raise ValueError("Seletor inválido")
        print(f'\n\n\nBot: \t{principal[seletor][0]}')
        for resposta in range(1, len(principal[seletor])):
            if callable(principal[seletor][resposta]):
                principal[seletor][resposta]()
            else:
                print(f'\t {resposta}: {principal[seletor][resposta]}')
    except (ValueError, TypeError) as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def escolha(seletor):
    opcao = input("Selecione uma opção: ")
    if not opcao.isnumeric():
        print("Escolha um número. Tente novamente.")
        return True
    opcao = int(opcao)
    seletor = int(seletor)
    if seletor not in principal:
        print("Opção inválida.")
        return True
    if opcao == len(principal[seletor]) - 1:
        return False
    if opcao <= 0 or opcao > len(principal[seletor]):
        print("Opção inválida. Tente novamente.")
        return True
    if callable(fundo1[seletor][opcao]):
        fundo1[seletor][opcao]()
    else:
        print(fundo1[seletor][opcao])
    return True

def clean_input(nome):
    nome = clean_nome(nome)
    pergunta = input(f"{nome}: ")
    translator = str.maketrans('', '', string.punctuation)
    pergunta = pergunta.translate(translator).lower()
    pergunta = unidecode(pergunta)
    return pergunta

def clean_nome(nome):
    nome = nome.split()
    nome = nome[0].capitalize()
    return nome

# função para gerar 3 strings aleatórias a partir da função clean input
def limitar_busca(entrada):
    pergunta = entrada.split()
    print(random.sample(pergunta, 3))

def responder(pergunta, nome_usuario):
    # Tokenizar a pergunta em palavras
    palavras_pergunta = set(pergunta.split())

    for chave, resposta in fundo2.items():
        palavras_chave = set(chave.lower().split())
        # Verificar se pelo menos 3 palavras da pergunta estão na chave
        if len(palavras_pergunta.intersection(palavras_chave)) >= 3:
            return print(f"Bot: "+resposta)

    return print(f"Desculpe {clean_nome(nome_usuario)}, não entendi sua pergunta.")