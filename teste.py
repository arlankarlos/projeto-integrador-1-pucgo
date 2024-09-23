# import string
from banco_de_respostas import fundo2

# text = "Hello world, welcome to the universe."
# words_to_find = ("world", "welcome", "universe", "arlan")
# translator = str.maketrans('', '', string.punctuation)
# text = text.translate(translator).lower()
# result = all(word in text.split() for word in words_to_find)
# print(result)

# import random

# text = "Olá, mUnDo! Você está aprendendo PyThOn? É fÁcil e divertido."
# palavras = text.split()  # Cria uma lista de palavras

# # Seleciona 3 palavras aleatórias da lista
# palavras_aleatorias = random.sample(palavras, 3)
# print(palavras_aleatorias)

# def responder(pergunta):
#     resposta = fundo2.get(pergunta, "Desculpe, não entendi sua pergunta.")
#     return resposta

# pergunta_usuario = "qual o seu nome?"
# resposta_bot = responder(pergunta_usuario)
# print(resposta_bot)

def responder2(pergunta):
    # Tokenizar a pergunta em palavras
    palavras_pergunta = set(pergunta.lower().split())

    for chave, resposta in fundo2.items():
        palavras_chave = set(chave.lower().split())
        # Verificar se pelo menos 3 palavras da pergunta estão na chave
        if len(palavras_pergunta.intersection(palavras_chave)) >= 2:
            return resposta

    return "Desculpe, não entendi sua pergunta."

pergunta = "qual é seu nome"
resposta = responder2(pergunta)
print(resposta)  # Saída: Meu nome é Assistente!