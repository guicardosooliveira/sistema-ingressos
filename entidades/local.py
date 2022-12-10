class Local:
    def __init__(self, rua: str, cep: int, lotacao_maxima: int):
        self.__rua = rua
        self.__cep = cep
        self.__lotacao_maxima = lotacao_maxima


    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, nova_rua):
        self.__rua = nova_rua

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self,novo_cpf):
        self.__cep = novo_cpf

    @property
    def lotacao_maxima (self):
        return self.__lotacao_maxima

    @lotacao_maxima.setter
    def lotacao_maxima(self,nova_lotacao_maxima):
        self.__lotacao_maxima = nova_lotacao_maxima
