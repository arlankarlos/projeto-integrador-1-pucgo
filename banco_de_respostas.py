from respostas_util import *

principal = {

    1: {0:"Fico feliz que faça parte da nossa família.\n\tEscolha:",
        1:"Emitir boleto de mensalidade.",
        2:"Emitir comprovante de matricula.",
        3:"Emitir certificado de conclusão de curso.",
        4:"Indicar amigos para estudar na PUC-GO.",
        5:"Voltar."},
    2: {0:"Você deseja fazer parte da nossa família. Escolha:",
        1:"Prova presencial.",
        2:"Prova online.",
        3:"Nota do ENEM",
        4:"Diploma ou transferência",
        5:"Conhecer nossos cursos?",
        6:"Voltar."},
}

fundo1 ={
    1:{ 1:"Boleto de mensalidade emitido.",
        2:"Comprovante de matricula emitido.",
        3:emitir_certificado,
        4:"https://www.pucgoias.edu.br/estude-na-puc/",
        },

    2:{ 1:"https://www.pucgoias.edu.br/estude-na-puc/ingresse-atraves-de-prova-presencial/",
        2:"https://www.pucgoias.edu.br/estude-na-puc/ingresse-atraves-de-prova-online",
        3:"https://www.pucgoias.edu.br/estude-na-puc/enem/",
        4:"https://www.pucgoias.edu.br/estude-na-puc/ingresse-atraves-de-transferencia-e-segunda-graduacao/",
        5:"https://www.pucgoias.edu.br/cursos-de-graduacao/",},

    3:{ 1:"Acesse o site da PUC-GO.",
        2:"Conheça nossos cursos.",
        3:"Receba o contato da PUC-GO.",}}

