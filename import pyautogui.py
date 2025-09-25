with open("aluno.txt", "r")as arq:
    for linha in arq:
        print(linha.strip())