class CpfEmUsoException(Exception):
    def __init__(self):
        super().__init__("O cpf fornecido está vinculado a outra conta. Tente Novamente.")