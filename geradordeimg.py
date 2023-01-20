import openai
from decouple import config

token = config('TOKEN')

openai.api_key = token

response = openai.Image.create(
    prompt='garden with tools',
    n=1,
    size='512x512'
)

url = response['data'][0]['url']

print(f'Url da imagem: {url}')