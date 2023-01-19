import os
import openai
from decouple import config

token = config('TOKEN')
openai.api_key = token


while True:
    print('Bem vindo(a) ao Chat, para parar digite: "stop".')
    print(' ')

    ask = input('Pergunte o que quiser: ')
    if ask == 'stop':
        break

    response = openai.Completion.create(

    model="text-davinci-003",
    prompt=ask,
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=[" Human:", " AI:"]
    )

    text = response['choices'][0]['text']

    print('Resposta: ' + text)
