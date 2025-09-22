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
'''

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

    