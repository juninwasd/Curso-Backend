#100 a 200#
# 14 Crie duS Variáveis:

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
teste= (a in az)
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
