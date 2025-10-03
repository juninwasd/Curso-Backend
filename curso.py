class Curso:
    def __init__( self, nome):
        self.nome = nome
        self.alunos = set()
        self.professores = set()