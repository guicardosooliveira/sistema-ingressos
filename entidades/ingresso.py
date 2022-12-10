class Ingresso:
    def __init__(self, valor: float, codigo: int, evento: str):
        self.__valor = valor
        self.__codigo = codigo
        self.__evento = evento
        self.__comprador = None

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor):
        self.__valor = novo_valor

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def evento(self):
        return self.__evento

    @evento.setter
    def evento(self, evento):
        self.__evento = evento

    @property
    def comprador(self):
        return self.__comprador

    @comprador.setter
    def comprador(self, novo_comprador):
        self.__comprador = novo_comprador
