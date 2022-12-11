class CpfNotFoundException(Exception):
    def __init__(self):
        super().__init__("Não existe uma conta cadastrada com esse CPF.")