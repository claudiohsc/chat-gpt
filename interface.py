from PySimpleGUI import PySimpleGUI as sg


#Criando Layout

sg.theme('Dark Blue 3')
layout = [
    [sg.Text('Digite sua pergunta/frase'),sg.Input(key='pergunta')],
    [sg.Button('Enviar')]
]

#Criando a janela

janela = sg.Window('Chat GPT-3', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Enviar':
        texto = valores['pergunta']
        print(texto)