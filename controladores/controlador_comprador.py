from entidades.comprador import Comprador
from telas.tela_comprador import TelaComprador


class ControladorComprador:
    def __init__(self, controlador_principal, controlador_evento, controlador_ingressos):
        self.__controlador_principal = controlador_principal
        self.__controlador_evento = controlador_evento
        self.__controlador_ingressos = controlador_ingressos
        self.__compradores = []
        self.__tela_comprador = TelaComprador()
        self.__tela_aberta = False

    def comprar_ingresso(self):
        self.__controlador_evento.listar_eventos()
        button, codigo_evento = self.__tela_comprador.pega_dados_para_compra_ingresso()
        ingresso = None
        for evento in self.__controlador_evento.eventos:
            if codigo_evento["input_codigo_evento"] == evento.codigo:
                if len(evento.ingressos) > 0:
                    ingresso = evento.ingressos[0]
                    evento.ingressos.remove(ingresso)
                    evento.ingressos_vendidos.append(ingresso)
                    self.__controlador_principal.usuario_logado.meus_ingressos.append(ingresso)
                    self.__tela_comprador.mostra_mensagem("Ingresso comprado com sucesso!")
                    self.mostrar_opcoes_comprador()

                else:
                    self.__tela_comprador.mostra_mensagem("Os ingressos para o evento fornecido estão esgotados")
        if not ingresso:
            self.__tela_comprador.mostra_mensagem("O código de evento fornecido não existe")

    # pronto

    @property
    def compradores(self):
        return self.__compradores

    def inclui_comprador(self, values):
        nome = values['input_nome']
        cpf = values['input_cpf']
        email = values['input_email']
        celular = values['input_celular']
        senha = values['input_senha']

        comprador = Comprador(nome, cpf, email, celular, senha)

        try:
            for i in self.__compradores:
                if comprador.cpf == i.cpf:
                    raise SystemError
            else:
                self.__compradores.append(comprador)
                self.__controlador_principal.altera_usuario_logado(comprador)
                self.mostrar_opcoes_comprador()

                return comprador
        except SystemError:
            self.__tela_comprador.mostra_mensagem("O cpf fornecido está vinculado a outra conta. Tente Novamente.")

    def mostrar_opcoes_comprador(self):
        button, values = self.__tela_comprador.mostrar_opcoes()
        opcoes = {'Ver meus ingressos': self.ver_meus_ingressos,
                  'Ver eventos disponíveis': self.ver_eventos_disponiveis,
                  'Comprar ingresso': self.comprar_ingresso,
                  'Excluir conta': self.excluir_comprador,
                  'Sair da conta': self.sair_da_conta}
        opcoes[button]()

    def ver_meus_ingressos(self):
        self.__controlador_ingressos.listar_ingressos()
        self.mostrar_opcoes_comprador()

    def ver_eventos_disponiveis(self):
        self.__controlador_evento.listar_eventos()
        self.mostrar_opcoes_comprador()

    def excluir_comprador(self):
        usuario_para_excluir = self.__controlador_principal.usuario_logado
        self.__compradores.remove(usuario_para_excluir)
        self.sair_da_conta()

    def sair_da_conta(self):
        self.__controlador_principal.altera_usuario_logado(None)
        self.__controlador_principal.inicializa_sistema()

    def retorna_comprador_pelo_cpf(self, cpf):
        for comprador in self.__compradores:
            if comprador.cpf == cpf:
                return comprador
        return None
