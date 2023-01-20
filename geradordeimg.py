import openai
from decouple import config

token = config('TOKEN')

openai.api_key = token

response = openai.Image.create(
    prompt='a cat programming',
    n=1,
    size='1024x1024'
)

url = response['data'][0]['url']

print(f'Url da imagem: {url}')