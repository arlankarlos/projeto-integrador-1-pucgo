import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
meu_email = os.environ["EMAIL_PESSOAL"]
minha_senha = os.environ["SENHA_EMAIL_PESSOAL"]


def envia_email(corpo, destinatario, assunto):
    # Cria mensagem
    """
    Envia um email com o corpo, destinatário e assunto recebidos como parâmetro.

    :parâmetro corpo: O conteúdo do email
    :type corpo: str
    :parâmetro destinatario: O email do destinatário
    :type destinatario: str
    :parâmetro assunto: O assunto do email
    :type assunto: str
    """
    mensagem = MIMEText(corpo)
    mensagem["From"] = meu_email
    mensagem["To"] = destinatario
    mensagem["Subject"] = assunto
    try:
        # Conecta ao servidor SMTP do Gmail e envia a mensagem
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(meu_email, minha_senha)
            smtp.sendmail(meu_email, destinatario, mensagem.as_string())
        return True
    except smtplib.SMTPException as e:
        print(f"Erro: {e}")
        input("Contate o admistrador para configurar o servidor SMTP.\nEnter para continuar.")
        return False


def emitir_certificado():
    """
    Requere um certificado com o nome, matrícula, curso e data de conclusão do aluno.

    :parâmetro nome: O nome do aluno
    :type nome: str
    :parâmetro matricula: A matrícula do aluno
    :type matricula: str
    :parâmetro curso: O curso do aluno
    :type curso: str
    :parâmetro data_de_conclusao: A data de conclusão do curso do aluno
    :type data_de_conclusao: str
    """
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    curso = input("Curso: ")
    data_de_conclusao = input("Data de conclusão do seu curso: ")
    print("\n" + "_" * 20)
    print(
        f"Certificado Requerido, aguardar confecção.\nNome: {nome} \nMatrícula: {matricula} \nCurso: {curso} \nData de conclusão: {data_de_conclusao}"
    )
    print("_" * 20 + "\n")


def emitir_boleto():
    """
    Emite um boleto com o nome, email e matrícula do aluno.

    :parâmetro nome: O nome do aluno
    :type nome: str
    :parâmetro email: O email do aluno
    :type email: str
    :parâmetro matricula: A matrícula do aluno
    :type matricula: str
    """
    nome = input("Nome: ")
    email = input("Email: ")
    matricula = input("Matrícula: ")
    print("\n" + "_" * 20)
    print(
        f"Boleto emitido.\nNome: {nome} \nEmail: {email} \nMatrícula: {matricula}\nValor: R$ XXX,XX\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
    )
    print("_" * 20 + "\n")


def indicar_amigo():
    """
    Indica um amigo para o PUC-GO.

    :parâmetro nome_indicador: O nome do indicador
    :type nome_indicador: str
    :parâmetro email_indicador: O email do indicador
    :type email_indicador: str
    :parâmetro nome_amigo: O nome do amigo
    :type nome_amigo: str
    :parâmetro email_amigo: O email do amigo
    :type email_amigo: str
    :parâmetro telefone_amigo: O telefone do amigo
    :type telefone_amigo: str
    """
    nome_indicador = input("Seu nome: ")
    email_indicador = input("Email: ")
    print("Dados do amigo: ")
    nome_amigo = input("Nome: ")
    email_amigo = input("Email: ")
    telefone_amigo = input("Telefone: ")

    # Informações para envio de e-mail
    assunto = "Indicado por {}".format(nome_indicador)
    corpo = f"{nome_amigo}, você foi convidado por {nome_indicador} para o PUC-GO. \n\nEm breve entraremos em contato.\nEmail: {email_amigo}\nTelefone: {telefone_amigo}\n\n\n\nSeja PUC-GO."
    destinatario = envia_email(corpo, email_amigo, assunto)
    remetente = envia_email(corpo, email_indicador, assunto)
    if destinatario and remetente:
        print("\n" * 3 + "_" * 20)
        print(
            f"Entraremos em contato\nNome: {nome_amigo} \nEmail: {email_amigo} \nTelefone: {telefone_amigo}"
        )
        print("_" * 20 + "\n")
    else:
        print("\n" + "_" * 20)
        print("Erro ao enviar e-mail")
        print("_" * 20 + "\n")


def emitir_comprovante():
    """
    Emite um comprovante de matrícula com o nome, email, matrícula e curso do aluno.

    :parâmetro nome: O nome do aluno
    :type nome: str
    :parâmetro matricula: A matrícula do aluno
    :type matricula: str
    :parâmetro curso: O curso do aluno
    :type curso: str
    :parâmetro email: O email do aluno
    :type email: str
    """
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    curso = input("Curso: ")
    email = input("Email: ")
    # Informações para envio de e-mail
    assunto = f"Matrícula: {matricula}"
    corpo = f"COMPROVANTE DE MATRÍCULA PUC-GO\n\nDeclaro para os devidos fins que {nome}, está devidamente matriculado no curso de {curso.upper()}, sob a matricula {matricula}.\n\n\nGoiânia, {datetime.now().strftime('%d/%m/%Y')} \nPUC-GO."
    destinario = envia_email(corpo, email, assunto)
    if destinario:
        print("\n" + "_" * 20)
        print(
            f"Comprovante de matrícula enviado por e-mail ({email}).\nNome: {nome} \nMatrícula: {matricula}"
        )
        print("_" * 20 + "\n")
    else:
        print("\n" + "_" * 20)
        print("Erro ao enviar e-mail")
        print("_" * 20 + "\n")
