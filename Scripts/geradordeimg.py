import openai
from decouple import config

token = config('TOKEN')

openai.api_key = token
res = str(input('Digite um texto para gerar uma imagem: '))
response = openai.Image.create(
    prompt=res,
    n=1,
    size='256x256'
)

url = response['data'][0]['url']

print(f'Url da imagem: {url}')