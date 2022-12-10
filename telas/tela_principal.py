import PySimpleGUI as sg


class TelaPrincipal:
    def __init__(self):
        self.__window = None

    def escolher_login_ou_cadastro(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text('Bem-vindo ao tickets.com', size=(40, 2))],
            [sg.Button('Registre-se')],
            [sg.Button('Login')],
        ]

        self.__window = sg.Window('Sistema de Ingressos').Layout(layout)
        button, values = self.__window.read()
        self.close()

        return button

    def tela_login(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Login")],
            [sg.Text("Digite seus dados:")],
            [sg.Text("Cpf", size=(15, 1)), sg.InputText(key='input_cpf')],
            [sg.Text("Senha", size=(15, 1)), sg.InputText(key='input_senha')],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('Sistema de Ingressos').Layout(layout)
        button, values = self.__window.read()
        self.close()

        return button, values

    def tela_cadastro(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Cadastre-se")],
            [sg.Text("Digite seus dados:")],
            [sg.Text("Nome", size=(15, 1)), sg.InputText(key='input_nome')],
            [sg.Text("Cpf", size=(15, 1)), sg.InputText(key='input_cpf')],
            [sg.Text("Email", size=(15, 1)), sg.InputText(key='input_email')],
            [sg.Text("Celular", size=(15, 1)), sg.InputText(key='input_celular')],
            [sg.Text("Senha", size=(15, 1)), sg.InputText(key='input_senha')],
            [sg.Text("Como voce deseja se cadastrar?")],
            [sg.Button("Comprador"), sg.Button("Produtor")],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('Sistema de Ingressos').Layout(layout)
        button, values = self.__window.read()
        self.close()

        return button, values

    def open(self):
        button, values = self.__window.Read()
        print(button)
        print(values)
        return button, values

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()