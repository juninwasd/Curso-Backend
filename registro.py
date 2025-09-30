'''
class ContaBancaria:
    def __init__(self,titular,saldo):
        self.__titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def depositar(self,valor):
        self.__saldo += valor

conta = ContaBancaria("Ana", 1000)
print(conta.get_saldo())
conta.depositar(500)
print(conta.get_saldo())

class Animal:
    def __init__(self,nome):
        self.nome = nome
    
    def emitir_som(self):
        print("Som Genérico...")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")
        
class Humano(Animal):
    def emitir_som(self):
        print("Olá ")

dog = Cachorro("Rex")
cat = Gato("Mimi")
humano = Humano("José")

dog.emitir_som()
cat.emitir_som()
humano.emitir_som()


class Funcionário:
    def __init__(self,nome,salário):
        self.nome = nome
        self.__salário = salário

    def get_salário(self):
        return self.__salário
    
    def set_salário(self,novo_salário):
        if novo_salário > 0:
            self.__salário = novo_salário
        else:
            print("Salário invalido")
        
    def mostrar_dados(self):
        print(f"Nome: {self.nome} | Salário: R${self.__salário:.2f}")

class Gerente(Funcionário):
        
    def __init__(self,nome,salario,departamento):
        Funcionário.__init__(self, nome, salario)
        self.departamento = departamento
        
    def mostrar_departamento(self):
        return (f"O Gerente {self.nome} é responsável pelo departamento de  {self.departamento}.")


funcionário = Funcionário("Ana", 1500)
funcionário.mostrar_dados()
funcionário.set_salário(2500)
print("Novo salário:", funcionário.get_salário())

gerente = Gerente("José Alves", 5000, "Vendas")
gerente.mostrar_dados()
gerente.mostrar_departamento()


class Produto:
    def __init__(self,nome,preço):
        self.__nome = nome
        self.__preço = preço
    
    def get_preço(self):
       return self.__preço
    
    def descontos(self):
        self.__preço *=0.9
          

produtoa = Produto("Celular", 5000)
produtob = Produto("Notebook", 7000)


print("Sem desconto:" ,produtoa.get_preço())
produtoa.descontos()
print("Com desconto:" ,produtoa.get_preço())

print("Sem desconto:"  ,produtob.get_preço())
produtob.descontos()
print("Com desconto:"  ,produtob.get_preço())



class Veiculo:
    def __init__(self,marca,ano):
        self.marca = marca
        self.ano = ano
    
class Carro(Veiculo):
    def mostrar_tipo(self):
        print(f"{self.marca} {self.ano} é um carro")

class Moto(Veiculo):
    def mostrar_tipo(self):
        print(f"{self.marca} {self.ano} é uma Moto")

c1 = Carro("Fiat", 2020)
m1 = Moto("Honda", 2022)

c1.mostrar_tipo()
m1.mostrar_tipo()
'''

class Funcionario:
    def __init__(self):
    def trabalhar():




class Estagiario(Funcionario):
    def trabalho():











