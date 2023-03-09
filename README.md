# API Chat-GPT

Esse repositório utiliza da API da Open AI para gerar textos que sejam o mais próximo da linguagem humana.


## Código base da API do Chat-Gpt

De início foi gerado um script simples para gerar textos a partir de perguntas e instruções. (Arquivo: /Scripts/main.py)

Depois de configurar o Token da API podemos utilizá-la.

```python

openai.api_key = token

```

O código abaixo é uma representação bruta de como podemos fazer isso:

```python

pergunta = input('Pergunte o que quiser: ')

response = openai.Completion.create(

    model="text-davinci-003",
    prompt=pergunta,
    temperature=0.5,
    max_tokens=1024,
    )

    text = response['choices'][0]['text']

```

A variável "text" retornará o que a IA nos trouxe de acordo com a instrução.
Para modificar o tamanho dessa saída definimos um número maior para o "max_tokens".
