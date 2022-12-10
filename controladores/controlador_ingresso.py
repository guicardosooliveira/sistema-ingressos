from entidades.ingresso import Ingresso


class ControladorIngresso:
    def __init__(self):
        self.__ingressos = []

    @property
    def ingresso(self):
        return self.__ingressos

    def gerar_ingressos(self, lotacao, evento, valor):
        quantidade_de_ingressos = 0
        ingressos_gerados = []
        while quantidade_de_ingressos < int(lotacao):
            ingresso_novo = Ingresso(valor, quantidade_de_ingressos, evento.nome)
            ingressos_gerados.append(ingresso_novo)
            quantidade_de_ingressos += 1
        self.__ingressos.append(ingressos_gerados)

        return ingressos_gerados

    def excluir_ingressos(self):
        pass

    def listar_ingressos(self):
        pass

    def alterar_ingressos(self):
        pass
