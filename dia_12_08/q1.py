nome = input("Digite seu nome: ")
disciplina = input("Digite a disciplina: ")
nota = float(input("Digite a nota: "))
status = ''

if nota <0 or nota >10:
    print("Nota inválida, tente novamente!")
else:
    if nota >= 5.5 and nota <= 5.9 :
        nota = 6.0
    if nota >= 0 and nota < 6:
        status = "REPROVADO"
    elif nota > 5 or nota < 11: 
        status = "APROVADO"
    print(f"{nome} está {status} em {disciplina} com {nota}")