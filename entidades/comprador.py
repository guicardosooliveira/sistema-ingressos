from entidades.usuario import Usuario


class Comprador(Usuario):
    def __init__(self, nome: str, cpf: int, email: str, celular: int, senha: str):
        super().__init__(nome, cpf, email, celular, senha)
        self.__historico_compras = []
        self.__eventos_favoritos = []
        self.__meus_ingressos = []

    @property
    def historico_compras(self):
        return self.__historico_compras

    @property
    def eventos_favoritos(self):
        return self.__eventos_favoritos

    @property
    def meus_ingressos(self):
        return self.__meus_ingressos
