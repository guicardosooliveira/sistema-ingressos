from entidades.usuario import Usuario


class Produtor(Usuario):
    def __init__(self, nome: str, cpf: int, email: str, celular: int, senha: str):
        super().__init__(nome, cpf, email, celular, senha)
        self.__historico_eventos = []

    @property
    def historico_eventos(self):
        return self.__historico_eventos

