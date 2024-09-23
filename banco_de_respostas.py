from respostas_util import *


principal = {

    1: {0:"Eu fico feliz que faça parte da nossa família.\n\tEscolha:\n",
        1:"Emitir boleto de mensalidade.",
        2:"Emitir comprovante de matricula.",
        3:"Emitir certificado de conclusão de curso.",
        4:"Indicar amigos para estudar na PUC-GO.",
        5:"Voltar."},
    2: {0:"Você deseja fazer parte da nossa família. \n\tEscolha:\n",
        1:"Prova presencial.",
        2:"Prova online.",
        3:"Nota do ENEM",
        4:"Diploma ou transferência",
        5:"Conhecer nossos cursos?",
        6:"Voltar."},
    3: {0:"Eu sou um assistente virtual da PUC-GO. \n\tComo posso te ajudar?\n",
        1: "A verificar.",
        2: "Voltar"}
}

fundo1 ={
    1:{ 1:emitir_boleto,
        2:emitir_comprovante,
        3:emitir_certificado,
        4:indicar_amigo,
        },

    2:{ 1:"https://www.pucgoias.edu.br/estude-na-puc/ingresse-atraves-de-prova-presencial/",
        2:"https://www.pucgoias.edu.br/estude-na-puc/ingresse-atraves-de-prova-online",
        3:"https://www.pucgoias.edu.br/estude-na-puc/enem/",
        4:"https://www.pucgoias.edu.br/estude-na-puc/ingresse-atraves-de-transferencia-e-segunda-graduacao/",
        5:"https://www.pucgoias.edu.br/cursos-de-graduacao/",},

    3:{ 1:"Eu sou um assistente virtual da PUC-GO. Como posso te ajudar?"}
}

fundo2={
    "como vai voce": "Eu vou um assistente virtual, estou sempre bem =D, obrigado. Como posso te ajudar?",
    "qual o seu nome": "Meu nome é Bot PUC-Goiááás! Prazer em te conhecer.",
    "voce gosta de musica": "Sim, adoro música! Qual o seu gênero musical favorito?",
    "qual a hora agora": "A hora atual é: " + str(datetime.now().time().strftime("%H:%M:%S")),  # Utiliza datetime para obter a hora atual
    }
