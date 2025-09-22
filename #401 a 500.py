#401 a 500

#dicionario - dict
dict = {"nome": "Ana","idade": 25,"cidade": "São Paulo"}

print(dict["nome"])

print(dict.get("altura"))

print(dict.get("altura", 0))

dict["idade"] = 26
dict["profissão"] = "engenharia"

(dict.keys())
(dict.values())
(dict.items())

aluno ={
        "nome": "Carlos",
        "notas": [7.5,8, 9]
}
print(aluno.items())


pessoa = (input("Atribui seu nome: "))
pessoa1 = (input("Atribui sua idade: "))
pessoa2 = (input("Atribui sua cidade: "))

pessoa = {
        "nome": [pessoa],
        "idade": [pessoa1],
        "cidade": [pessoa2]
}
print(pessoa)

mercado = {
        "banana": 3.50,
        "maça": 2.80,
        "uva": 4.00

#""""
}
print (sum(mercado.values()))


frase = "o rato roeu a roupa do rei de roma e a rainha de raiva roeu o resto"
palavra = frase.split()
dicionario = {}
for coisa in palavra:
    if coisa in dicionario:
        dicionario[coisa]+= 1
    else:
        dicionario[coisa]= 1

print (dicionario)

compromisso = {"Dom pedro I":["19 00000-0001","19 0000-0002"],"Pedro Alvares Cabral":["19 00000-0129","19 00000-0130"]}

for contato,telefones in compromisso.items():
    print(f"{contato}:")
    for telefone in telefones:
        print(f"  - {telefone}")
  

def greet():
    print('Hello words!')

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Júnio")

#""""
def soma(a,b):
    return a + b
resultado = soma(3, 5)
print (resultado)

#criar progama
def calcula_imc(peso, altura):
    imc = (peso/altura**2)
    return imc 
def classificar_imc(imc):
    if imc < (18.5):
     return("Abaixo do peso")
    elif imc < (24.9):
     return("peso normal")
    elif imc < (29.9):
     return("Sobrepeso")
    elif imc < (39.9):
     return("Obesidade")
    else:
     return("Obesidade grave")

def main():
    peso = float(input("Define sua Massa(kg): "))
    altura = float(input("Define sua Altura(m): "))
    imc = calcula_imc(peso, altura)
    classificação = classificar_imc(imc)
    print(f"Seu imc é: {imc:.2f}")
    print(f"Classificação: {classificação}")

main()
