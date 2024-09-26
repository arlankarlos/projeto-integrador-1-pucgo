from banco_de_respostas import principal, fundo1, fundo2
import random
import string
from unidecode import unidecode
# chaves para controle do while
chave_interna = True
chave_externa = True

def menu():
    """
    Função que imprime o menu principal do programa, oferecendo quatro opções ao
    usuário: se ele é aluno da PUC-GO, se ele deseja se tornar aluno,
    se ele deseja saber mais sobre o bot e a opção de encerrar o programa.
    """
    menu = """\n\n\n\n\n
Bot:    Você é aluno da PUC-GO?

        1: Sim, sou PUC-GO.
        2: Ainda não sou PUC-GO, mas quero muito de ser!
        3: Oi bot. Quem é você?
        4: Encerrar.
    """
    print(menu)

def menu_escolhido(seletor):
    """
    Função que imprime o menu escolhido pelo usuário, oferecendo as opções
    correspondentes ao seletor informado.

    Parameters
    ----------
    seletor : int
        Número do menu escolhido pelo usuário.

    Returns
    -------
    None
    """
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
    """
    Função que permite ao usuário escolher uma opção de menu.

    Parameters
    ----------
    seletor : int
        Número do menu escolhido pelo usuário.

    Returns
    -------
    bool
        True se a escolha for inválida, False caso contrário.
    """
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
    """
    Função que limpa a entrada do usuário, removendo pontuações e
    convertendo para minúsculas. Retorna uma string com a pergunta
    tratada.

    Parameters
    ----------
    nome : str
        Nome do usuário

    Returns
    -------
    str
        Pergunta tratada
    """
    nome = clean_nome(nome)
    pergunta = input(f"{nome}: ")
    translator = str.maketrans('', '', string.punctuation)
    pergunta = pergunta.translate(translator).lower()
    pergunta = unidecode(pergunta)
    return pergunta

def clean_nome(nome):
    """
    Função que limpa o nome do usuário, removendo sobrenomes e 
    convertendo para maiúscula a primeira letra. Retorna uma string 
    com o nome do usuário tratado.

    Parameters
    ----------
    nome : str
        Nome do usuário

    Returns
    -------
    str
        Nome do usuário tratado
    """
    nome = nome.split()
    nome = nome[0].capitalize()
    return nome

# função para gerar 3 strings aleatórias a partir da função clean input
def limitar_busca(entrada):
    """
    Função que recebe uma entrada e retorna 3 strings aleatórias a partir 
    da entrada.

    Parameters
    ----------
    entrada : str
        Entrada do usuário

    Returns
    -------
    list
        3 strings aleatórias a partir da entrada
    """
    pergunta = entrada.split()
    print(random.sample(pergunta, 3))

def responder(pergunta, nome_usuario):
    # Tokenizar a pergunta em palavras
    """
    Função que recebe uma pergunta e um nome de usuário e retorna uma 
    resposta. A resposta é buscada em um dicionário com palavras chaves 
    e respostas. Se a pergunta contiver pelo menos 3 palavras da chave, 
    retorna a resposta. Caso contrário, retorna uma mensagem de erro.

    Parameters
    ----------
    pergunta : str
        Pergunta do usuário
    nome_usuario : str
        Nome do usuário

    Returns
    -------
    None
    """
    palavras_pergunta = set(pergunta.split())

    for chave, resposta in fundo2.items():
        palavras_chave = set(chave.lower().split())
        # Verificar se pelo menos 3 palavras da pergunta estão na chave
        if len(palavras_pergunta.intersection(palavras_chave)) >= 3:
            return print(f"Bot: "+resposta)

    return print(f"Desculpe {clean_nome(nome_usuario)}, não entendi sua pergunta.")