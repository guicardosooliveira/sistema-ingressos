class CodigoEmUsoException(Exception):
    def __init__(self):
        super().__init__("Código de evento já cadastrado.")