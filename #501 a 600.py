#501 a 600

class pessoa:
    def __init__(self,nome,idade,):
        self.nome = nome
        self.idade = idade    
    def apresentar(self):
        print(f"Olá ,eu nome é {self.nome} e tenho {self.idade} anos.")
    def fazer_aniversáio(self):
        self.idade += 1
        print(f"\n----Minha idade daqui 1 ano é {self.idade}-----\n")    

p1 = pessoa("Júnio", 30)
p2 = pessoa("eduardo", 25)
p1.apresentar()
p2.apresentar()
p1.fazer_aniversáio()
p1.apresentar()
p2.apresentar()

class ContaBancaria:
    def __init__(self,titular):
        self.titular = titular
        self.saldo = 0

    def depositar_valor(self,valor):
        self.saldo += valor
        print(f"\nVoçê acabou de depositar {valor:.2f} realizado com sucesso.")

    def sacar_valor(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("\nVoçê acabou de sacar  {valor:.2f} da sua conta!")
        else:
            print("\nVoçê não tem saldo suficiente")

    def mostrar_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

conta = ContaBancaria("Marco")
conta.depositar_valor(500)
conta.sacar_valor(200)
conta.sacar_valor(400)
conta.mostrar_saldo()
