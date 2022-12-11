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
            [sg.Button('Comprar ingresso')],
            [sg.Button('Excluir conta')],
            [sg.Button('Sair da conta')],
        ]

        self.__window = sg.Window('Sistema de Ingressos').Layout(layout)
        button, values = self.__window.read()
        self.close()

        return button, values

    def pega_dados_para_compra_ingresso(self):
        print("chegou aqui")
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("---Compra de Ingressos---")],
            [sg.Text("Digite o código do evento que deseja comprar:")],
            [sg.InputText(key="input_codigo_evento")],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('Comprar ingresso').Layout(layout)
        button, values = self.__window.read()
        self.close()

        #tratamento de dados
        codigo = values["input_codigo_evento"]
        try:
            if button == "Submit" and (codigo == "" or not codigo.isdigit()):
                raise ValueError
            else:
                return button, values
        except ValueError:
            return None, None

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()