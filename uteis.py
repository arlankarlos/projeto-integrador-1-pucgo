from banco_de_respostas import principal, fundo1
# chaves para controle do while
chave_interna = True
chave_externa = True

def menu():
    menu = """
        Você é aluno da PUC-GO?
        1: Sim, sou PUC-GO.
        2: Ainda não sou PUC-GO, mas quero muito de ser!
        3: Encerrar.
    """
    print(menu)

def menu_escolhido(seletor):
    try:
        seletor = int(seletor)
        if seletor not in principal:
            raise ValueError("Seletor inválido")
        print(f'Bot: \t{principal[seletor][0]}')
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




# class Aluno:
#     def __init__(self, nome, cpf, media):
#         self.nome = nome
#         self.cpf = cpf
#         self.media = media

#     def __str__(self):
#         return f'Nome: {self.nome}\nCPF: {self.cpf}\nMedia: {self.media}'

#     def criar_aluno(self, nome, cpf):
#         self.nome = nome
#         self.cpf = cpf

#     def media_aluno(self, nota1, nota2):
#         self.media = (nota1 + nota2) / 2