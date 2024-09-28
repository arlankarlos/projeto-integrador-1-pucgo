from banco_de_respostas import principal, fundo1, fundo2
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
    menu = """\n
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

    Parâmetros
    ----------
    seletor : int
        Número do menu escolhido pelo usuário.

    Retorno
    -------
    None
    """
    try:
        # Conversão para inteiro: O valor de seletor é convertido para
        # um inteiro para garantir que seja um número válido.
        seletor = int(seletor)

        # Verificação de existência: A função verifica se o seletor corresponde
        # a um menu existente no dicionário principal.
        if seletor not in principal:
            raise ValueError("Seletor inválido")

        # Impressão do título do menu: O título do menu é impresso
        # na tela utilizando f-strings.
        print(f"\nBot: \t{principal[seletor][0]}")

        # Iteração sobre as opções: A função itera sobre as opções do menu selecionado.
        for resposta in range(1, len(principal[seletor])):
            # Opções executáveis: Se a opção for uma função (callable), ela é executada
            # diretamente. Isso permite que o menu contenha opções que executam ações específicas.
            if callable(principal[seletor][resposta]):
                principal[seletor][resposta]()
            else:
                # Cada opção é impressa na tela utilizando f-strings.
                print(f"\t {resposta}: {principal[seletor][resposta]}")
        """
        BLOCO EXCEPT
        Tratamento de erros: A função utiliza múltiplos blocos except
        para capturar diferentes tipos de exceções que podem ocorrer
        durante a execução.

        ValueError: É lançada quando o valor de seletor não é um
        número inteiro válido ou quando o valor não corresponde a
        um menu existente.

        TypeError: Pode ser lançada se houver algum problema com
        o tipo de dado de principal[seletor].
        Exception: Captura qualquer outro tipo de exceção não
        tratada nos blocos anteriores.
        """
    except (ValueError, TypeError) as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def escolha(seletor):
    """
    Função que permite ao usuário escolher uma opção de menu.

    Parâmetros
    ----------
    seletor : int
        Número do menu escolhido pelo usuário.

    Retorno
    -------
    bool
        True se a escolha for inválida, False caso contrário.
    """
    opcao = input("Selecione uma opção: ")

    # Validar a entrada: Verifica se a entrada do usuário é
    # um número válido e se a opção escolhida existe dentro do menu.
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

    # Verifica se é uma função: Se a opção correspondente for
    # uma função (callable), ela é executada.
    if callable(fundo1[seletor][opcao]):
        fundo1[seletor][opcao]()
    else:
        print(fundo1[seletor][opcao])
    return True
    # Retornar True/False para controle de fluxo: A função retorna True
    # se a escolha for inválida e False caso contrário. True mantem
    # dentro do loop para filtrar por escolhas válidas.


def clean_input(nome):
    """
    Função que limpa a entrada do usuário, removendo pontuações e
    convertendo para minúsculas. Retorna uma string com a pergunta
    tratada.

    Parâmetros
    ----------
    nome : str
        Nome do usuário

    Retorno
    -------
    str
        Pergunta tratada
    """
    nome = clean_nome(nome)
    pergunta = input(f"{nome}: ")

    # Remoção de pontuação: Emprega str.maketrans e translate
    # para eliminar todos os caracteres de pontuação.
    translator = str.maketrans("", "", string.punctuation)
    pergunta = pergunta.translate(translator).lower()

    # Remoção de acentos: Utiliza unidecode para remover os acentos das letras.
    pergunta = unidecode(pergunta)
    return pergunta


def clean_nome(nome):
    """
    Função que limpa o nome do usuário, removendo sobrenomes e
    convertendo para maiúscula a primeira letra. Retorna uma string
    com o nome do usuário tratado.

    Parâmetros
    ----------
    nome : str
        Nome do usuário

    Retorno
    -------
    str
        Nome do usuário tratado
    """
    nome = nome.split()
    nome = nome[0].capitalize()
    return nome


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

    Retorno
    -------
    None
    """
    # Quebra da pergunta em palavras: A pergunta do usuário é dividida
    # em palavras individuais e armazenada em um conjunto (set) para
    # facilitar as comparações.
    # Tokenizar a pergunta em palavras.
    palavras_pergunta = set(pergunta.split())

    for chave, resposta in fundo2.items():
        # Tokenizar a chave em palavras.
        palavras_chave = set(chave.lower().split())

        # Verificação de correspondência: Se pelo menos 3 palavras da pergunta
        # estiverem presentes nas palavras-chave da entrada, considera-se que
        # a pergunta foi entendida e a resposta correspondente é retornada.
        if len(palavras_pergunta.intersection(palavras_chave)) >= 3:
            return print(f"Bot: {resposta}")

    return print(f"Desculpe {clean_nome(nome_usuario)}, não entendi sua pergunta.")
