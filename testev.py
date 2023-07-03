import openai
from pydantic import BaseModel

class Document(BaseModel):
    prompt: str = ''

def inference(prompt: str) -> list:

    #Tokens
    openai.organization = 'org-UMvDyRx65jNBwUOR1SBlThZl'
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40, '-'))

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres una calculadora, si se ingresa un numero calcularas el factorial de dicho numero "
            E.G: 10
            -claro el factorial de 4! = 4 * 3 * 2 * 1 = 24.
            E.G: hola
            - error"""
             },
            {"role": "user", "content": prompt}
        ]
    )

    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    print("Tokens utilizados: " + total_tokens)
    return [content, total_tokens]