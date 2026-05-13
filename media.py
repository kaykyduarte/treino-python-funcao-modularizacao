from cadastrar import cadastro

def media():
    aluno, nota1, nota2 = cadastro()
    media = (nota1 + nota2) / 2

    return aluno, media


