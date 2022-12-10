import PySimpleGUI as sg


class TelaComprador:
    def __init__(self):
        self.__window = None

    def mostrar_opcoes(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text('Área do Comprador', size=(40, 2))],
            [sg.Button('Ver meus ingressos')],
            [sg.Button('Ver eventos disponíveis')],
            [sg.Button('Ver eventos favoritos')],
            [sg.Button('Favoritar evento')],
            [sg.Button('Remover evento dos favoritos')],
            [sg.Button('Comprar ingresso')],
            [sg.Button('Excluir conta')],
            [sg.Button('Sair da conta')],
        ]

        self.__window = sg.Window('Sistema de Ingressos').Layout(layout)
        button, values = self.__window.read()
        self.close()

        return button, values

    def pega_dados_para_compra_ingresso(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("---Compra de Ingressos---")],
            [sg.Text("Digite o código do evento que deseja comprar:")],
            [sg.InputText],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('Comprar ingresso').Layout(layout)
        button, values = self.__window.read()
        self.close()

        return button, values

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()