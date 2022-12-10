import PySimpleGUI as sg


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

        return button, values

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

        window = sg.Window('tickets.com').layout(layout)
        button, values = window.read()
        self.close()

        return button, values

    def remover_evento(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Exclusão de evento")],
            [sg.Text("Digite o código do evento que deseja editar"), sg.InputText(key='input_codigo')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('tickets.com').layout(layout)
        button, values = window.read()
        self.close()

        return button, values

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
