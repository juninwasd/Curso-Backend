#301 a 400

Lista_compras = []

while True:
    item = input("Digite um item para a lista de compras (ou sair para encerrar): ")

    if item.lower() == "sair":
        break
    else:
        Lista_compras.append(item)
print("\nItems na sua lista de compras: ")
for intem in Lista_compras:
    print(f" - {item}")
print(f"\nTotal de itens: {len(Lista_compras)}")

lista_ordenada = sorted(Lista_compras)
print("\nLista em ordem alfabética: ")
for item in lista_ordenada:
    print(f"- {item}")

    minha_tupla = 1, 2, 3
minha_tupla = (1, 2, 3)
minha_tupla_um = (1,)
não_tupla = (1)

x, y, z =(1,2,3)
print(x,y,z)

t = (1,2,2,2,4,5,3)
print(len(t))
print(t.index (3))
print(t.count (2))

#set
meu_conjunto = {1 ,"banana", 3.14, 1 }
print (meu_conjunto)

numeros =[10,11,12,12,13,14,14,15,10]
conj = set(numeros)
print(conj)

vazio = set()

a ={1,2,3}
b = {3,4,5}
uniao = a|b
print ("uniao:", uniao)
uniao = a.union(b)
print ("uniao:", uniao)

diferença = a-b
print("diferença:", diferença)

interseção = a&b
print("interseção:", interseção)

interseção = a.intersection(b)
print("interseção:", interseção)

c= {1,2,3}

c.add(2)
c.remove(2)
c.discard(2)
c.clear()

lista_1 = ["ana","Carlos","João"]
lista_2 = ["Maria","Carlos","Pedro"]

conj1 = set(lista_1)
conj2 = set(lista_2)

comum = conj1.intersection(conj2)
print (comum)

lista_1 = ["ana","Carlos","João"]
lista_2 = ["Maria","Carlos","Pedro"]

conj1 = set(lista_1)
conj2 = set(lista_2)

comum = (conj1-conj2)
print (comum)


frase =input("Peça ao voçê que me fale uma frase: ")
variavel= frase.split()
print(variavel)

conj= set(variavel)
print(conj)


palavra = (input("Digite a palavra: "))
if len(palavra) ==  len(set(palavra)):
          print("Palavra semelhante")
else:
          print("Palavras repetidas") 
