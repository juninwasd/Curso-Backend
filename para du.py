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
c.remove(10)
c.discard(2)
c.clear()







