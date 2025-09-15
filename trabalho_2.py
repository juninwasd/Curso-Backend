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
   numero = float(input("digite um número(0 para parar):" ))
   if numero == 0:
      break
   soma += numero
print ("A soma dos numeros é:", soma)
   
