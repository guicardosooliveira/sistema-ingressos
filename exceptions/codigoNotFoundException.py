class CodigoNotFoundException(Exception):
    def __init__(self):
        super().__init__("Não existe um evento com o código inserido, favor tente novamente.")