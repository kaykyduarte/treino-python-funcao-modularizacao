from media import media 


def verificar():
    aluno, resultado = media()
    if resultado >=6:
        status = 'Aprovado'
    else: 
        status = 'Reprovado'
    return aluno, resultado, status 

print(verificar())
    