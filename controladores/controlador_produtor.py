from entidades.produtor import Produtor
from telas.tela_produtor import TelaProdutor


class ControladorProdutor:
    def __init__(self, controlador_principal, controlador_evento):
        self.__controlador_principal = controlador_principal
        self.__controlador_evento = controlador_evento
        self.__produtores = []
        self.__tela_produtor = TelaProdutor()
        self.__tela_aberta = False

    @property
    def produtores(self):
        return self.__produtores

    def inclui_produtor(self, values):
        nome = values['input_nome']
        cpf = values['input_cpf']
        email = values['input_email']
        celular = values['input_celular']
        senha = values['input_senha']

        produtor = Produtor(nome, cpf, email, celular, senha)
        try:
            for i in self.__produtores:
                if produtor.cpf == i.cpf:
                    raise SystemError
            else:
                self.__produtores.append(produtor)
                self.__controlador_principal.altera_usuario_logado(produtor)
                self.mostrar_opcoes_produtor()

                return produtor
        except SystemError:
            self.__tela_produtor.produtor_ja_existe()

    def mostrar_opcoes_produtor(self):
        button, values = self.__tela_produtor.mostrar_opcoes()
        opcoes = {'Adicionar evento': self.adicionar_evento,
                  'Ver meus eventos': self.listar_meus_eventos,
                  'Editar meus eventos': self.editar_evento,
                  'Excluir meus eventos': self.remover_evento,
                  'Histórico de eventos': self.mostrar_historico_eventos,
                  'Excluir conta': self.excluir_produtor,
                  'Sair da conta': self.sair_da_conta}
        opcoes[button]()

    def adicionar_evento(self):
        evento = self.__controlador_evento.adicionar_evento()

        if self.__controlador_evento.retorna_evento_pelo_codigo(evento.codigo):
            self.incluir_no_historico_eventos(evento.nome, evento.codigo, evento.ingressos[0].valor)

        else:
            self.__tela_produtor.mostra_mensagem('Evento ja existe')

        self.mostrar_opcoes_produtor()

    def listar_meus_eventos(self):
        self.__controlador_evento.listar_eventos()
        self.mostrar_opcoes_produtor()

    def editar_evento(self):
        self.__controlador_evento.editar_evento()
        self.mostrar_opcoes_produtor()

    def remover_evento(self):
        self.__controlador_evento.remover_evento()
        self.mostrar_opcoes_produtor()

    def mostrar_historico_eventos(self):
        historico_de_eventos = self.__controlador_principal.usuario_logado.historico_eventos

        self.__controlador_evento.listar_eventos_de_um_produtor(historico_de_eventos)
        self.mostrar_opcoes_produtor()

    def excluir_produtor(self):
        usuario_para_excluir = self.__controlador_principal.usuario_logado
        self.__produtores.remove(usuario_para_excluir.cpf)
        self.sair_da_conta()

    def sair_da_conta(self):
        self.__controlador_principal.inicializa_sistema()

    def listar_produtores(self):
        return self.__produtores

    def incluir_no_historico_eventos(self, nome, codigo, valor):
        self.__controlador_principal.usuario_logado.historico_eventos.append([nome, codigo, valor])

    def retorna_produtor_pelo_cpf(self, cpf):
        for produtor in self.__produtores:
            if produtor.cpf == cpf:
                return produtor
        return None
