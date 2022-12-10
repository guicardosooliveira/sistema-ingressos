import PySimpleGUI as sg

class TelaIngresso:
    def __init__(self):
        self.__window = None


    def pega_dados(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Dados dos ingressos")],
            [sg.Text("Digite os dados dos ingressos:")],
            [sg.Text("Valor", size=(15, 1)), sg.InputText(key='input_valor')],
            [sg.Text("Lote", size=(15, 1)), sg.InputText(key='input_lote')],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('tickets.com').layout(layout)
        button, values = self.__window.read()

        return button, values


    def alterar_ingresso(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Edição de ingressos")],
            [sg.Text("Digite o nome do evento dos ingressos que deseja editar"), sg.InputText(key='input_nome')],
            [sg.Text("Digite os dados atualizados:")],
            [sg.Text("Valor", size=(15, 1)), sg.InputText(key='input_novo_valor')],
            [sg.Text("Lote", size=(15, 1)), sg.InputText(key='input_novo_lote')],
            [sg.Text("Código dos ingressos", size=(15, 1)), sg.InputText(key='input_novo_codigo')],
            [sg.Text("Nome do evento", size=(15, 1)), sg.InputText(key='input_novo_nome')],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('tickets.com').layout(layout)
        button, values = self.__window.read()

        return button, values