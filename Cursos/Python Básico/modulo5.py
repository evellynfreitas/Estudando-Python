def lerNota():
    nota = float(input("Digite a nota do aluno: "))
    return nota
    
def calculaMedia(n1,n2,n3):
    media = n1 + n2 + n3
    media = media / 3
    print("Média: ", media)
    if(media >= 7):
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")


a = lerNota()
b = lerNota()
c = lerNota()
calculaMedia(a,b,c)