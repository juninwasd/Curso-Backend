#1 Calcular a soma de 15 + 27

a= 15
b = 27
soma= (a+b)
print ('Resultado pergunta 1.:', soma)

#2 Multiplique 12 por 8

c = 12
d = 8
Multiplicação= (c*d)
print ('Resultado pergunta 2.:', Multiplicação)

#3 Divide 25 por 4 e veja o resultado

e = 25
f = 4
Divisão= (e/f)
print ('Resultado pergunta 3.:', Divisão)

#4 Descubra o resto da divisão de 37 por 5

g = 37
h = 5
resto= (g%h)
print ('Resultado pergunta 4.:', resto)

#5 Eleve 3 à potência de 4

i = 3
j = 4
potencia= (i**j)
print ('Resultado pergunta 5.:', potencia)

#6 Verifique se 10 é maior que 7

k = 10
l = 7

Maior= (k > l)
print ('Resultado pergunta 6.:',Maior)

#7 Verifique se 15 é igual a 20

m = 10
n = 7

Igual= (m == n)
print ('Resultado pergunta 7.:',Igual)

#8 Teste se 100 é menor ou igual a 100

o = 100
p = 100

Menor_ou_igual = (o <= p)
print ('Resultado pergunta 8.:',Menor_ou_igual)

#9 Veja se 45 é diferente de 30

q = 45
r = 30

Diferente= (q != p)
print ('Resultado pergunta 9.:',Diferente)

#10 Verifique se 5>2 e 8>3

s = 5
t = 2 
u = 8
v = 3

AND= (s>t and u>v)
print ('Resultado pergunta 10.:',AND)

#11 Verifique se 10<3 ou 4==4

w = 10
x = 3 
y = 4
z = 3

OR= (w>x or y>z)
print ('Resultado pergunta 11.:',OR)

#12 Inverta o resultado lógico de (7>2) usando not

aa = 7
ab = 2

NOT= not(aa>ab)
print ('Resultado pergunta 12.:',NOT)

#13 Crie uma Variável x com valor 10. Depois faça:

X = 10

X= (X + 5)
print ('Parte 1.:',X)

X= (X * 2)
print ('Parte 2.:',X)

X= (X - 4)
print ('Parte Total.:',X)

#14 Crie duS Variáveis:

a = [1,2,3]
b = a
c = [1,2,3]

Variável= (a is b)
print ('Resultado pergunta 14.:',Variável)

Verifique= (a is c)
print ('Resultado pergunta 15.:',Verifique)

#ou

print(f"""    14. Verifique se (a is b):{a is b}
    14. Verifiquese se (a is c):{a is c}""")

print ("o valor é:", a)
print ("o valor de A é:", a, "e o valor de B é", b)
print (f"o valor de A é:{a} e o valor de B é:{b}")

print ("""        podemos imprimir
        multiplas linhas
        na saída do print""")

#15. Teste se oo número 3 está dentro da lista [1,2,3,4,5]

ay = [1,2,3,4,5]
Teste= (3 in ay)
print ('Teste.:',Teste)

#16. Teste se a letra 'z' está dentro da palavra "casa".

az = ["casa"]
teste= (z in az)
print ("teste 1.:",teste)

#1
Nome= input("Digite seu nome:" )
Idade= int(input("Digite sua idade:" ))

#2
a=(100)
calcular_seculo= (a - Idade)
print ("A sua idade daqui a 100 anos: ", calcular_seculo)

#3
o = 18

Maior_ou_igual = (Idade >= o)
print ('maioridade:',Maior_ou_igual)

#4
s = [13,14,15,16,17,18,19]

Adolescente= (Idade in s)
print ('Adolescente.:',Adolescente)

#5
X = Idade

X= (X + 5)
print ('Idade daqui 5 anos:',X)

#6
teste= ("a" in Nome)
print ("se seu nome tem a letra A:",teste)

#Positivo e Negativo
x= 0

if x > 0:
    print ("Numero Positivo")
elif x == 0:
    print ("Numero zero")
else:
     print ("Numero Negativo")
#Uma nota de 0 a 100
nota = 100
if nota >= 90:
        print("excelência")
elif nota >= 60:
        print("Aprovado")
else:
     print("Reprovado")

#Maioridade e Menoridade
Idade= 123

if Idade <= 13:
    print("Criança")
elif Idade <= 17: 
    print("Adolescente")
else:
    print("Adulto")

#
Contador = 1
while Contador <= 10:
    print("número:", Contador)
    Contador +=1

#
for i in range (2,22,2):

    print (i)
 #
numero_1 =int(input("numero 1=") )
numero_2 =int(input("numero 2=") )
numero_3 =int(input("numero 3=") )
numero_4 =int(input("numero 4=") )
numero_5 =int(input("numero 5=") )

#
soma= (numero_1+numero_2+numero_3+numero_4+numero_5)
print(soma)

#
for i in range(1,11):
 soma= (i*7)
 print (f"7 x {i} = {7 * i}")


#
soma = 0
while True:
   numero = int(input("digite um número(0 para parar):" ))
   if numero == 0:
      break
   elif numero == "":
      break
   soma += numero
print ("A soma dos numeros é:", soma)
   
try:
   x = 5/1
except ZeroDivisionError:
   print("Divisão por zerp não permitido")
else:
   print("Divisão realizado com sucesso")
finally:
   print("Este bloco sempre será executado")

L=[20 ,"Junio", 13.14, 20,]
frutas= [ "maça", 'banana','laranja']
print (frutas[2])
numeros = list(range (1,4))
for fruta in frutas:
    print(fruta)
#
list = [1,2,3]
list.append(4)
print(list)
#
list = [1,2,3]
list.insert(1, "a")
print(list)
#
list = [1,2]
list.extend([3,4])
print(list)
#
list = [1,2,3,2]
list.remove(2)
print(list)
#
list = [10,20,30]
valor=list.pop()
print(list)
#
valor=list.pop(0)
print(list)
#
list = [1,2,3,2]
list.clear()
print(list)
#
list = ["a","b","c","b"]
list.index("b")
print(list)
#
list.index("b", 2)
print(list)
#
list = [1,2,3,4]
list.count(2)
print(list)
#
list = [4,3,2,1]
list.sort()
print(list)
#
list.sort(reverse=True)
print(list)
#
list = [3,1,4]
nova= sorted(list)
print(list, nova)
#
list = [3,1,4]
list.copy()
print(list)
#
soma=[1,2] + [3,4]
print(soma)
#
repetição=[0]* 5
print(repetição)
#


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

numeros = [1,2,2,3,4,4,5,1]
sem_duplicatas = list(set(numeros))
print("lista sem duplicatas: "), sem_duplicatas



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













































































































































































