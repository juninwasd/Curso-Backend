from abc import ABC, abstractmethod
import math

#
class Forma(ABC):
    @abstractmethod
    def Metodo_area(self):
        pass

class Retangulo(Forma):
    def Metodo_area(self,base,altura):
        self.base = base
        self.altura = altura
        return self.base*self.altura
        
class Circulo(Forma):
    def Metodo_area(self,raio):
        self.raio = raio
        return math.pi*(self.raio^2)

p1 = Retangulo()
print (f"Area do Retangulo é igual a: {p1.Metodo_area(10, 10)}")

p2 = Circulo()
print (f"Area do circulo é igual a: {p2.Metodo_area(10)}")

'''

#
class Funcionario(ABC):
    @abstractmethod
    def calcular_pagamento(self):
        pass


class Assaláriado(Funcionario):
    def __init__(self, salario):
        self.salario = salario
    
    def calcular_pagamento(self):
        return self.
     
    
class Horista(Funcionario):
    def calcular_pagamento(self):
        return f"Seu salário sera de R$ 15 , durante 9  horas , que dará R$ 135"

funcionario = [Assaláriado(),Horista()]

for r in funcionario:
    print(r.calcular_pagamento())

#
class Instrumento(ABC):
    @abstractmethod
    def tocar(Self):
        pass

class Violao(Instrumento):
    def tocar(self):
        return "Toco Violão"
    
class Bateria(Instrumento):
    def tocar(self):
        return "Toco Bateria"

Instrumento = [Violao(),Bateria()]

for t in Instrumento:
    print(t.tocar())

#
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

class Carro(Transporte):
    def mover(self):
        return "O carro anda pelas estradas"
    
class Aviao(Transporte):
    def mover(self):
        return "O avião voa pelos céus"
    
class Barco(Transporte):
    def mover(self):
        return "O barco navegas pelas entradas"
    
Transporte = [Carro(),Aviao(),Barco()]

for t in Transporte:
    print(t.mover())

#
class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"    
    
class Pato:
    def fazer_som(self):
        return "Quack!"
    
animais = [Cachorro(),Gato(),Pato()]

for animal in animais:
    print(animal.fazer_som())
'''