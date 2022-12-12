import PySimpleGUI as sg


class TelaProdutor:
    def __init__(self):
        self.__window = None

    def mostrar_opcoes(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text('Área do produtor', size=(40, 2))],
            [sg.Button('Adicionar evento')],
            [sg.Button('Ver meus eventos')],
            [sg.Button('Editar meus eventos')],
            [sg.Button('Excluir meus eventos')],
            [sg.Button('Histórico de eventos')],
            [sg.Button('Excluir conta')],
            [sg.Button('Sair da conta')],
        ]

        self.__window = sg.Window('Sistema de Ingressos').Layout(layout)
        button, values = self.__window.read()
        self.close()

        return button, values

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()