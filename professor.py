from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, cpf, siape):
        super().__init__(nome, cpf)
        self.siape = siape
        