from PySimpleGUI import PySimpleGUI as sg
import openai
from decouple import config

token = config('TOKEN')
openai.api_key = token


#Criando Layout

sg.theme('Black')
layout = [
    [sg.Text('Digite sua pergunta/frase:'), sg.Input(key='pergunta', size=(50, 4))],
    [sg.Push(), sg.Button('Enviar'), sg.Push()],
    [sg.Push(),sg.Text('Resposta do Chat-GPT:'), sg.Push()],
    [sg.Push(), sg.Output(size=(60,20)), sg.Push()]
]

#Criando a janela

janela = sg.Window('Chat GPT-3', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Enviar':
        texto = valores['pergunta']

        #integrando chat-gpt para responder
        response = openai.Completion.create(

            model="text-davinci-003",
            prompt=texto,
            temperature=0.5,
            max_tokens=1024,
            )

        text = response['choices'][0]['text']

        print(text)
        