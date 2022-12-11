from telas.tela_evento import TelaEvento
from entidades.evento import Evento
from entidades.local import Local
from exceptions.codigoEmUsoException import CodigoEmUsoException
from exceptions.codigoNotFoundException import CodigoNotFoundException


class ControladorEvento:
    def __init__(self, controlador_ingressos):
        self.__eventos = []
        self.__tela_evento = TelaEvento()
        self.__controlador_ingressos = controlador_ingressos

    @property
    def eventos(self):
        return self.__eventos

    def adicionar_evento(self):
        deu_certo = False
        while not deu_certo:

            button, dados_evento = self.__tela_evento.adiciona_evento()
            if button == "Cancel":
                return None
            elif button is None and dados_evento is None:
                self.__tela_evento.mostra_mensagem("Os dados inseridos estão incorretos, favor preencher novamente.")
            else:
                try:
                    deu_certo = True
                    data = f'{dados_evento["input_dia_evento"]}/{dados_evento["input_mes_evento"]}/{dados_evento["input_ano_evento"]}'
                    local = Local(dados_evento['input_rua'], dados_evento['input_cep'], dados_evento['input_lotacao'])
                    evento = Evento(dados_evento['input_codigo'], data, dados_evento['input_nome'], local)

                    if not self.retorna_evento_pelo_codigo(evento.codigo):
                        self.__eventos.append(evento)
                        ingresso_gerados = self.__controlador_ingressos.gerar_ingressos(dados_evento["input_lotacao"], evento,
                                                                                        dados_evento["input_valor"])

                        evento.ingressos = ingresso_gerados
                        return evento

                    else:
                        raise CodigoEmUsoException
                except CodigoEmUsoException:
                    self.__tela_evento.mostra_mensagem('Codigo de evento ja cadastrado')

    def listar_eventos_de_um_produtor(self, eventos):
        self.__tela_evento.mostrar_eventos(eventos)

    def listar_eventos(self):
        eventos = []
        for evento in self.__eventos:
            if len(evento.ingressos) > 0:
                eventos.append([evento.nome, evento.codigo, evento.ingressos[0].valor])
            else:
                continue
        self.__tela_evento.mostrar_eventos(eventos)

    def retorna_evento_pelo_codigo(self, codigo):
        for evento in self.__eventos:
            if evento.codigo == codigo:
                return evento
        return None

    def editar_evento(self):
        deu_certo = False
        self.listar_eventos()
        while not deu_certo:
            button, dados_atualizados = self.__tela_evento.alterar_evento()
            if button == "Cancel":
                break
            elif button is None and dados_atualizados is None:
                self.__tela_evento.mostra_mensagem("Os dados inseridos estão incorretos, favor preencher novamente.")
            else:
                try:
                    deu_certo = True
                    data = f'{dados_atualizados["input_dia_evento"]}/{dados_atualizados["input_mes_evento"]}/{dados_atualizados["input_ano_evento"]}'
                    evento_a_ser_alterado = None
                    for evento in self.__eventos:
                        if evento.codigo == dados_atualizados["input_codigo_pra_alterar"]:
                            evento_a_ser_alterado = evento

                    if evento_a_ser_alterado:
                        evento_a_ser_alterado.codigo = (dados_atualizados['input_codigo'])
                        evento_a_ser_alterado.data = data
                        evento_a_ser_alterado.nome = (dados_atualizados['input_nome'])
                    else:
                        raise CodigoNotFoundException
                except CodigoNotFoundException:
                    self.__tela_evento.mostra_mensagem("Não existe um evento com o código inserido, favor tente novamente.")

    def remover_evento(self):
        deu_certo = False
        self.listar_eventos()
        while not deu_certo:
            button, values = self.__tela_evento.remover_evento()

            if button == "Cancel":
                break
            elif button is None and values is None:
                self.__tela_evento.mostra_mensagem("Os dados inseridos estão incorretos, favor preencher novamente.")
            else:
                try:
                    deu_certo = True
                    codigo_evento_para_ser_excluido = values['input_codigo']

                    if not self.retorna_evento_pelo_codigo(codigo_evento_para_ser_excluido):
                        raise CodigoNotFoundException
                    else:
                        evento = self.retorna_evento_pelo_codigo(codigo_evento_para_ser_excluido)
                        self.__eventos.remove(evento)
                        self.__tela_evento.mostra_mensagem('Evento excluído com sucesso!')
                        return evento
                except CodigoNotFoundException:
                    self.__tela_evento.mostra_mensagem('Não existe um evento com o código inserido, favor tente novamente.')
                    return None
