class Agenda:
    instrucao = 0
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        Agenda.instrucao += 1