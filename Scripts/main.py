import openai
from decouple import config

token = config('TOKEN')
openai.api_key = token

print('Bem vindo(a) ao Chat, para parar digite: "stop".')
print(' ')

while True:

    pergunta = input('Pergunte o que quiser: ')
    if pergunta == 'stop':
        break

    response = openai.Completion.create(

    model="text-davinci-003",
    prompt=pergunta,
    temperature=0.5,
    max_tokens=1024,
    )

    text = response['choices'][0]['text']

    print('Resposta: ' + text)
