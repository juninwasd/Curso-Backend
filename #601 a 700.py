#601 a 700
''''
class Vendedor:
    def __init__(self,nome,meta,vendas):
        self.meta = meta
        self.vendas = vendas
        self.nome = nome
        
    def bateu_meta(self):
        if self.vendas >= self.meta:
            return ("Bateu Meta")
        else:
            return ("Não Bateu a Meta")
     

pessoa1 = Vendedor("fernando", 500 , 600) 
print (pessoa1.bateu_meta())


nome = 'fernando'
vendas = 400
meta = 500


class Vendedor:
    def __init__(self,nome,meta,vendas):
        self.meta = meta
        self.vendas = vendas
        self.nome = nome
        
    def bateu_meta(self):
        if self.vendas >= self.meta:
            return ("Bateu Meta")
        else:
            return ("Não Bateu a Meta")
'''


class Usuário:
    def __init__(self, nome , email , senha ):
        self.nome = nome
        self.email = email
        self.senha = senha

    def exibir_dados(self):
        print (f"Seu nome de usuário é: {self.nome}")
        print (f"Seu email do usuário é: {self.email}")
    
    def alterar_senha(self):
        print (f"Sua senha atual é: {self.senha}")
        self.senha = input ("Digite a nova senha: ")
        print (f"Sua nova senha é : {self.senha}")

    def autenticador(self,email,senha):
        if (self.email == email and self.senha == senha):
            print("\n✔sucesso✔\n")
        else:
            print("\n✖errrrrrrou✖\n")


    def __str__(self):
        return (f"\nUsuário: {self.nome} - {self.email}")
        

conta = Usuário(input("\nDigite seu nome: "),input("Digite seu email: "),input("Digite sua senha: "))
print (conta.exibir_dados())
print (conta.alterar_senha())                
print (conta.autenticador(input("confirma email: "),input("confirma senha: ")))
print (conta.__str__())