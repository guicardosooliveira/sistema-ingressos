from entidades.ingresso import Ingresso
from telas.tela_ingresso import TelaIngresso


class ControladorIngresso:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_ingresso = TelaIngresso()
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

    def listar_ingressos(self):
        lista_ingressos = []
        for ingresso in self.__controlador_principal.usuario_logado.meus_ingressos:
            lista_ingressos.append([ingresso.evento, ingresso.codigo, ingresso.valor])
        self.__tela_ingresso.mostrar_ingressos(lista_ingressos)


