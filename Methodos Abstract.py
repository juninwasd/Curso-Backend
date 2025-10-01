from abc import ABC, abstractmethod









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
