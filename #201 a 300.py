#201 a 300

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

