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


class Funcionario:
    def trabalhar(self):
        print(f"O funcionario esta trabalhando normalmento.")

class Estagiario(Funcionario):
    def trabalhar(self):
        print(f"\nO estagiario esta aprendendo enquanto trabalha.")

f1 = Funcionario()
e1 = Estagiario()

f1.trabalhar()
e1.trabalhar()




class ContaCorrente:
    def __init__(self,nome):
        self._saldo = 0
        self._nome = nome

    def get_depositar(self,valor):
        self._saldo += valor
        print(f"Voçê depositou R$ {valor:.2f}.")
    
    def set_sacar_dinheiro(self,valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"Voçê acabou de sacar R${valor:.2f}")
        else:
            print(f"Saldo insuficiente para realizar o saque")

    def mostrar_saldo(self):
        print(f"Saldo atual de {self._nome}: R${self._saldo:.2f}")

conta = ContaCorrente("Júnio")
conta.get_depositar(700)
conta.set_sacar_dinheiro(200)
conta.set_sacar_dinheiro(700)
conta.mostrar_saldo()


class Aluno:
    def __init__(self,nome,nota):
        self._nome = nome
        self._nota = nota

    def mostrar_nota(self):
        print(f"{self._nome},sua nota foi {self._nota}")

    def apenas(self):
        if self._nota >= 0 and self._nota <= 10:
            print("nota aceita")
        else:
            print("nota inexistente") 

aluno = Aluno("Eduardo", -1)
aluno2 = Aluno("Raissa", 1)
aluno3 = Aluno("Júnio", 9)

aluno.mostrar_nota()
aluno.apenas()
aluno3.mostrar_nota()
aluno3.apenas()
aluno2.mostrar_nota()
aluno2.apenas()



class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
class Professor(Pessoa):
    def __init__(self, nome, idade, materia):
        super().__init__(nome, idade)    
        self.materia = materia

p1 = Professor("Carlos", 40 , "Matemática")
print(p1.nome, p1.idade, p1.materia)


class Veiculo:
    def mover(self):
        print("O Veículo está se movendo...")

class Carro(Veiculo):
    def mover(self):
        print ("é um carro")

class Bicicleta(Veiculo):
    def mover(self):
        print("é uma bicicleta")

carro = Carro()
bicicleta = Bicicleta()

carro.mover()
bicicleta.mover()


class Usuario:
    def __init__(self, senha):
        self.__senha = senha
    
    def login(self, senha):
        if senha == self.__senha:
            print("Login realizado com sucesso!")
        else:
            print("Login incorreto")

    def alterar_senha(self,antiga,nova):
        if antiga == self.__senha:
            self.__senha = nova
            print("Senha alterada com sucesso!")
        else:
            print("Senha antiga incorreta")

u1 = Usuario("1234")
u1.login("1234")
u1.alterar_senha("1234", "abcd")
u1.login("abcd")            
            


class Animal:
    def respirar(self):
        print("O animal está respirando.")

class Mamifero(Animal):
    def amamentar(self):
        print("O mamifero está amamentando.")
    
class Cachorro(Mamifero):
    def latir(self):
        print("O cachorro está latindo: Au au!")

dog = Cachorro()
dog.respirar()
dog.amamentar()
dog.latir()
'''