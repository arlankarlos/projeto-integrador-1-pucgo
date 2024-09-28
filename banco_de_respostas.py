from respostas_util import emitir_boleto, emitir_certificado
from respostas_util import emitir_comprovante, indicar_amigo
from datetime import datetime


principal = {
    1: {
        0: "Eu fico feliz que faça parte da nossa família.\n\tEscolha:\n",
        1: "Emitir boleto de mensalidade.",
        2: "Emitir comprovante de matricula.",
        3: "Emitir certificado de conclusão de curso.",
        4: "Indicar amigos para estudar na PUC-GO.",
        5: "Voltar.",
    },
    2: {
        0: "Você deseja fazer parte da nossa família. \n\tEscolha:\n",
        1: "Prova presencial.",
        2: "Prova online.",
        3: "Nota do ENEM",
        4: "Diploma ou transferência",
        5: "Conhecer nossos cursos?",
        6: "Voltar.",
    },
    3: {
        0: "Eu sou um assistente virtual da PUC-GO. \n\tComo posso te ajudar?\n",
        1: "A verificar.",
        2: "Voltar",
    },
}

fundo1 = {
    1: {
        1: emitir_boleto,
        2: emitir_comprovante,
        3: emitir_certificado,
        4: indicar_amigo,
    },
    2: {
        1: "https://www.pucgoias.edu.br/estude-na-puc/ingresse-atraves-de-prova-presencial/",
        2: "https://www.pucgoias.edu.br/estude-na-puc/ingresse-atraves-de-prova-online",
        3: "https://www.pucgoias.edu.br/estude-na-puc/enem/",
        4: "https://www.pucgoias.edu.br/estude-na-puc/ingresse-atraves-de-transferencia-e-segunda-graduacao/",
        5: "https://www.pucgoias.edu.br/cursos-de-graduacao/",
    },
    3: {1: "Eu sou um assistente virtual da PUC-GO. Como posso te ajudar?"},
}

fundo2 = {
    "como esta vai voce tudo bem": "Estou sempre bem =D, obrigado. E você como está?",
    "eu estou bem vou": "Fico feliz que esteja bem!",
    "nao bem ruim mal mau triste": "Fico triste que esteja mal!",
    "qual o seu nome como se chama": "Meu nome é Bot PUC-Goiááás! Prazer em te conhecer.",
    "gosta de musica sertanejo classica": "Sim, adoro música! Qual o seu gênero musical favorito?",
    "qual hora agora quantas que horas sao": "A hora atual é: "
    + str(
        datetime.now().time().strftime("%H:%M:%S")
    ),  # Utiliza datetime para obter a hora atual
    "pode contar uma piada?": "Claro! Qual é o seu animal favorito? Um cão. E qual é o animal favorito de um cão? Um gato! Por quê? Porque os cães gostam de caçar gatos!",
    "ajudar encontrar uma receita?": "Com certeza! Qual tipo de comida você está procurando? Doce, salgada, vegetariana?",
    "dar previsão do tempo?": "Minha conexão GPS com o clima tempo falhou. Posso ajudar em algo mais?",
    "qual como fazer melhor receita pamonha": "Ingredientes: Milho verde fresco, leite de coco, açúcar, sal, folhas de milho. \nModo de preparo: Retire os grãos do milho e bata no liquidificador com o leite de coco, açúcar e sal. Coloque a massa nas folhas de milho, amarre bem e cozinhe em água fervente por cerca de 30 minutos.",
    "fazer receita brigadeiro": "Ingredientes: 1 lata de leite condensado, 1 colher de sopa de manteiga, 7 colheres de sopa de achocolatado em pó, chocolate granulado. \nModo de preparo: Em uma panela, misture o leite condensado, a manteiga e o achocolatado. Leve ao fogo baixo, mexendo sempre até desgrudar do fundo da panela. Deixe esfriar e faça bolinhas, passando no chocolate granulado.",
    "fazer receita pastel": "Ingredientes: 2 xícaras de farinha de trigo, 1 colher de sopa de óleo, 1 colher de chá de sal, 1/2 xícara de água morna. \nModo de preparo: Misture a farinha, o óleo e o sal. Adicione a água aos poucos, até formar uma massa homogênea. Abra a massa com um rolo e corte em círculos. Recheie e feche os pastéis com um garfo. Frite em óleo quente até dourar.",
    "fazer receita bolo milho": "Opção 1 - Simples: O bolo de milho é feito com milho verde, leite, ovos, açúcar, óleo e fermento. Misture tudo e asse em forno pré-aquecido.\nOpção 2 - Cremoso: Para um bolo de milho mais cremoso, adicione leite condensado à massa.",
    "fazer receita bolo fuba": "Para um bolo de fuba, adicione leite, farinha, ovo, o leite condensado e o creme de leite. Asse por 50 minutos em forno 200°C.",
    "fazer receita bolo vovo": "Opção 1 - Tradicional: O bolo da vovó é um clássico feito com farinha de trigo, açúcar, ovos, leite, fermento e essência de baunilha.\nOpção 2 - Modernizado: Que tal dar um toque moderno ao bolo da vovó? Adicione frutas vermelhas à massa ou prepare uma cobertura de chocolate.",
    "qual a receita de chica doida": "A chica doida é uma bebida refrescante feita com milho verde, açúcar e fermento. Deixe fermentar por alguns dias e sirva gelada.",
    "como fazer galinhada": "A galinhada é um prato saboroso feito com frango desfiado, arroz, legumes e temperos.",
    "qual a historia da PUC-GO": "Fundada em 1959, a PUC-GO é a universidade mais antiga de Goiás. Com um forte compromisso com a educação de qualidade, a instituição tem formado gerações de profissionais e pesquisadores, contribuindo significativamente para o desenvolvimento do estado.",
    "quais os cursos mais procurados na PUC-GO": "Os cursos mais procurados na PUC-GO incluem Direito, Medicina, Administração, Engenharia, Psicologia, Ciências Contábeis e Enfermagem. A universidade oferece uma ampla gama de opções de graduação e pós-graduação, adaptando-se às demandas do mercado de trabalho.",
    "quais os campi da PUC-GO": "A PUC-GO possui diversos campi em Goiânia, cada um com suas especificidades. O Campus I é o mais antigo e abriga a maioria dos cursos de graduação. O Campus II concentra-se nas áreas da saúde e bem-estar, enquanto o Campus III é dedicado aos cursos de pós-graduação e pesquisa.",
    "como é a vida estudantil na PUC-GO": "A vida estudantil na PUC-GO é marcada pela diversidade, engajamento e oportunidades. A universidade oferece uma ampla gama de atividades extracurriculares, como atléticas, culturais e sociais, além de programas de intercâmbio e projetos de pesquisa. Os estudantes têm acesso a uma infraestrutura moderna, bibliotecas bem equipadas e laboratórios de última geração.",
    "quais os diferenciais da PUC-GO": "A PUC-GO se destaca por seu corpo docente altamente qualificado, formado por mestres e doutores, que aliam conhecimento teórico e prático. A universidade também investe em pesquisa e inovação, promovendo a produção de conhecimento e o desenvolvimento de soluções para os desafios da sociedade.",
    "quais alguns ex-alunos famosos da PUC-GO": "A PUC-GO formou diversos profissionais que se destacaram em suas áreas de atuação. Entre eles, podemos citar [Nome de ex-alunos famosos da PUC-GO e suas respectivas áreas de atuação, por exemplo, políticos, empresários, artistas].",
    "quais as principais áreas de atuação dos ex-alunos da PUC-GO": "Os ex-alunos da PUC-GO atuam em diversas áreas, como direito, medicina, administração, engenharia, política, artes e cultura. Muitos ocupam cargos de liderança em empresas, órgãos públicos e instituições de ensino.",
    "existe algum programa de intercâmbio na PUC-GO": "Sim, a PUC-GO oferece diversos programas de intercâmbio para seus alunos, permitindo que eles vivenciem novas culturas e ampliem seus conhecimentos. A universidade mantém parcerias com instituições de ensino superior em diversos países.",
    "como o processo seletivo da PUC-GO": "O processo seletivo da PUC-GO geralmente envolve a realização de provas objetivas e discursivas, além da análise do histórico escolar. As vagas são disputadas através do Vestibular Tradicional ou do Sistema de Seleção Unificada (Sisu).",
    "quais as opcoes de pos-graduação na PUC-GO": "A PUC-GO oferece uma ampla gama de opções de pós-graduação, incluindo mestrados e doutorados em diversas áreas do conhecimento. A universidade também oferece cursos de especialização e MBA para profissionais que desejam se aperfeiçoar.",
    "o que big data": "O Big Data se refere a conjuntos de dados extremamente grandes e complexos que são difíceis de processar e analisar usando ferramentas de banco de dados tradicionais. Esses dados são caracterizados pelos 3 Vs: Volume, Velocidade e Variedade.",
    "quais os 5 vs do big data": "Além dos 3 Vs (Volume, Velocidade e Variedade), existem outros dois: Veracidade (qualidade e precisão dos dados) e Valor (o potencial dos dados para gerar insights e valor de negócio).",
    "quais as principais tecnologias utilizadas para trabalhar com big bata": "As principais tecnologias incluem Hadoop, Spark, NoSQL, Cloud Computing (AWS, Azure, GCP), ferramentas de visualização (Tableau, Power BI) e linguagens de programação como Python e R.",
    "quais as principais aplicacoes do big bata": "O Big Data tem diversas aplicações, como análise de redes sociais, recomendação de produtos, detecção de fraudes, otimização de marketing, previsão de demanda, análise de sentimentos, entre outras.",
    "como o big data é utilizado no marketing": "No marketing, o Big Data permite personalizar campanhas, analisar o comportamento do consumidor, medir a eficácia das ações e tomar decisões mais assertivas.",
    "qual o papel do big data na area da saude": "Na saúde, o Big Data é utilizado para analisar dados de pacientes, desenvolver novos tratamentos, personalizar a medicina e prevenir doenças.",
    "quais sao os principais desafios ao trabalhar com big data": "Os principais desafios incluem a gestão de grandes volumes de dados, a garantia da qualidade dos dados, a segurança da informação, a necessidade de profissionais qualificados e a complexidade das ferramentas.",
    "quais as oportunidades que o big data oferece para as empresas": "O Big Data oferece a oportunidade de tomar decisões mais inteligentes, otimizar processos, melhorar a experiência do cliente, desenvolver novos produtos e serviços e gerar vantagem competitiva.",
    "o que e Hadoop": "Hadoop é um framework open-source que permite o processamento distribuído de grandes conjuntos de dados em clusters de computadores.",
    "o que e Spark": "Spark é um framework de processamento de dados em memória, conhecido por sua velocidade e capacidade de executar análises complexas em grandes volumes de dados.",
    "o que e NoSQL": "NoSQL são bancos de dados não relacionais projetados para armazenar grandes volumes de dados estruturados, semiestruturados e não estruturados, oferecendo flexibilidade e escalabilidade.",
    "qual a diferenca entre big data e data science": "Big Data se refere aos dados em si, enquanto Data Science é a disciplina que utiliza técnicas estatísticas e de machine learning para extrair insights e conhecimento desses dados.",
    "quais sao as habilidades necessarias para trabalhar com big data": "As habilidades incluem programação (Python, R), estatística, machine learning, banco de dados, ferramentas de big data (Hadoop, Spark) e soft skills como comunicação e resolução de problemas.",
}
