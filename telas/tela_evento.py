import PySimpleGUI as sg
from datetime import datetime


class TelaEvento:
    def __init__(self):
        self.__window = None

    def adiciona_evento(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Cadastro de eventos")],
            [sg.Text("Digite os dados do evento:")],
            [sg.Text("Código", size=(15, 1)), sg.InputText(key='input_codigo')],
            [sg.Text("Dia do evento", size=(15, 1)), sg.InputText(key='input_dia_evento')],
            [sg.Text("Mes do evento", size=(15, 1)), sg.InputText(key='input_mes_evento')],
            [sg.Text("Ano do evento", size=(15, 1)), sg.InputText(key='input_ano_evento')],
            [sg.Text("Nome", size=(15, 1)), sg.InputText(key='input_nome')],
            [sg.Text("Rua do Local", size=(15, 1)), sg.InputText(key='input_rua')],
            [sg.Text("Cep", size=(15, 1)), sg.InputText(key='input_cep')],
            [sg.Text("Lotação", size=(15, 1)), sg.InputText(key='input_lotacao')],
            [sg.Text("Valor do ingresso", size=(15, 1)), sg.InputText(key='input_valor')],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('tickets.com').layout(layout)
        button, values = self.__window.read()
        self.close()

        # tratamento de dados
        codigo = values["input_codigo"]
        dia = values["input_dia_evento"]
        mes = values["input_mes_evento"]
        ano = values["input_ano_evento"]
        nome = values["input_nome"]
        rua = values["input_rua"]
        cep = values["input_cep"]
        lotacao = values["input_lotacao"]
        valor = values["input_valor"]

        try:
            data = f"{dia}/{mes}/{ano}"
            if button == "Cancel":
                return button, values, data
            elif button == "Submit" and (codigo == "" or dia == "" or mes == "" or ano == "" or nome == "" or rua == "" or
                                         cep == "" or lotacao == "" or valor == ""):
                raise ValueError
            elif button == "Submit" and ((not codigo.isdigit()) or (not cep.isdigit()) or (not lotacao.isdigit()) or
                                         (not valor.isdigit()) or (not dia.isdigit()) or (not mes.isdigit()) or
                                         (not ano.isdigit())):
                raise ValueError

            else:
                data_atualizada = datetime.strptime(data, "%d/%m/%Y")
                return button, values, data_atualizada
        except ValueError:
            return None, None, None

    def alterar_evento(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Edição de evento")],
            [sg.Text("Digite o código do evento que deseja editar"), sg.InputText(key='input_codigo_pra_alterar')],
            [sg.Text("Digite os dados atualizados:")],
            [sg.Text("Código", size=(15, 1)), sg.InputText(key='input_codigo')],
            [sg.Text("Dia do evento", size=(15, 1)), sg.InputText(key='input_dia_evento')],
            [sg.Text("Mes do evento", size=(15, 1)), sg.InputText(key='input_mes_evento')],
            [sg.Text("Ano do evento", size=(15, 1)), sg.InputText(key='input_ano_evento')],
            [sg.Text("Nome do evento", size=(15, 1)), sg.InputText(key='input_nome')],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('tickets.com').layout(layout)
        button, values = self.__window.read()
        self.close()

        # tratamento de dados
        codigo_para_alterar = values["input_codigo_pra_alterar"]
        codigo = values["input_codigo"]
        dia = values["input_dia_evento"]
        mes = values["input_mes_evento"]
        ano = values["input_ano_evento"]
        nome = values["input_nome"]

        try:
            data = f"{dia}/{mes}/{ano}"
            if button == "Cancel":
                return button, values, data
            elif button == "Submit" and (codigo_para_alterar == "" or codigo == "" or dia == "" or mes == "" or
                                       ano == "" or nome == ""):
                raise ValueError
            elif button == "Submit" and ((not codigo.isdigit()) or (not dia.isdigit()) or (not mes.isdigit()) or
                                         (not ano.isdigit()) or (not codigo_para_alterar.isdigit())):
                raise ValueError
            else:
                data_atualizada = datetime.strptime(data, "%d/%m/%Y")
                return button, values, data_atualizada
        except ValueError:
            return None, None, None

    def remover_evento(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Exclusão de evento")],
            [sg.Text("Digite o código do evento que deseja editar"), sg.InputText(key='input_codigo')],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('tickets.com').layout(layout)
        button, values = self.__window.read()
        self.close()

        # tratamento de dados
        codigo = values["input_codigo"]

        try:
            if button == "Submit" and codigo == "":
                raise ValueError
            elif button == "Submit" and (not codigo.isdigit()):
                raise ValueError
            else:
                return button, values
        except ValueError:
            return None, None

    def mostrar_eventos(self, eventos):
        string_todos_eventos = ''
        for evento in eventos:
            string_todos_eventos += evento[0]
            string_todos_eventos += ', código: '
            string_todos_eventos += evento[1]
            string_todos_eventos += ', R$'
            string_todos_eventos += evento[2]
            string_todos_eventos += '\n'
        sg.popup('-----LISTA DE EVENTOS-----', string_todos_eventos)

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()
