from abc import ABC, abstractmethod
import math

class Executar_movimento(ABC):
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






















'''
class Veiculo(ABC):
    @abstractmethod
    def abastecer(self):
        pass

class Carro(Veiculo):
    def abastecer(self):
        return "Carro abastece com Gasolina"


class Caminhão(Veiculo):
    def abastecer(self):
        return "Caminhão abastece com diesel"
        

veiculos = [Carro(),Caminhão()]

for n in veiculos:
    print(n.abastecer())







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



#
class Funcionario(ABC):
    @abstractmethod
    def calcular_pagamento(self):
        pass


class Assaláriado(Funcionario):
    def __init__(self, salario):
        self.salario = salario
    
    def calcular_pagamento(self):
        return self.salario
     
    
class Horista(Funcionario):
    def __init__(self, valor_hora, horas_trabalhados):
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhados
    
    def calcular_pagamento(self):
        return self.valor_hora * self.horas_trabalhadas


f1 = Assaláriado(3000)
f2 = Horista(50, 160)

print(f"Assalariado irá pagar {f1.calcular_pagamento()}")
print(f"Horista irá pagar {f2.calcular_pagamento()}")



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