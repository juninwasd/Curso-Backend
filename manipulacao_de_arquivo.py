'''
with open("alunos.txt", "r") as arq:
    for linha in arq:
        print(linha.strip())

with open("recado.txt", "w")as arq:
    arq.write("Essa mensagem será adicionada nova pasta\n")


linhas = ["João\n", "Maria\n", "Pedro\n"]

with open ("alunos.txt", "w") as arq:
    arq.writelines(linhas)

with open("nomes.txt", "r")as arq:
    for linha in arq:
        print(linha.strip()) # strip() remove \n

with open("nomes.txt", "r") as arq:
    nomes = arq.readline()

nomes_formatos= []
for n in nomes:
    n = n.strip().upper() + "\n"
    nomes_formatos.append(n)

with open("nomes.txt", "w") as arq:
    arq.writelines(nomes_formatos)




with open("novo.txt", "x") as arq:
    arq.write("arquivo novo")
'''

with open("usuarios.txt","r") as arq:
    linhas = arq.readline()

linhas_formatadas = []
for linha in linhas:
    nome,idade  = linha.strip().split(",")
    linhas_formatadas.append(f"{nome.upper()};{idade}\n")

with open("usuarios.txt","w") as arq:
    arq.writelines(linhas_formatadas)







