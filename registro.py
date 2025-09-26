
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
    
with open("usuario.txt","a") as arq:
 arq.write(f"{nome};{idade}\n")

