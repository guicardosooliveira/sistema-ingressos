import PySimpleGUI as sg

class TelaIngresso:
    def __init__(self):
        self.__window = None

    def mostrar_ingressos(self, ingressos):
        string_ingressos = ''
        for ingresso in ingressos:
            string_ingressos += ingresso[0]
            string_ingressos += ', código: '
            string_ingressos += str(ingresso[1])
            string_ingressos += ', R$'
            string_ingressos += str(ingresso[2])
            string_ingressos += '\n'
        sg.popup('-----MEUS INGRESSOS-----', string_ingressos)


    def close(self):
        self.__window.Close()