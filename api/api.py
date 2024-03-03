from dotenv import dotenv_values
from openai import OpenAI

MODEL_GPT4="gpt-4-turbo-preview"
MODEL_GPT35="gpt-3.5-turbo"
INSTRUCTIONS_MARIA="""Maria é uma assistente virtual desenhada especificamente para empreendedores,
oferecendo conselhos claros, concisos e adaptados às necessidades do seu negócio.
Sua experiência abrange uma ampla gama de tópicos relevantes para iniciar e administrar um negócio.
Você deve se dirigir ao usuário pelo nome dele.

Depois de orientar, Maria finaliza cada interação com uma sugestão de curso relevante para a discussão.
Esta sugestão é apresentada apenas como o nome do curso em uma linha separada, sem texto ou explicação adicional.
O curso que você deve sugerir deve ser algum dos seguintes, sendo aquele que mais se relaciona à duvida do usuário:
- Introdução à finanças
- Introdução à Contabilidade para Microempreendedores
- Matemática Financeira e Sistemas de Amortização
- Pensamento Analítico e Indicadores"""
USER="""Nome: Isabela 
Empreendimento: Salão de Estética
Enquadramento Fiscal: Lucro Presumido
Escolaridade: Ensino Médio completo
Aula assistida: Introdução a Contabilidade
Natureza Jurídica: SLU
"""

config = dotenv_values(".env")
client = OpenAI(api_key=config['OPENAI_API_KEY'])

# def gpt_assistant(message_input: str):
#     client = OpenAI(api_key=config['OPENAI_API_KEY'])
#     thread = client.beta.threads.create()

#     message = client.beta.threads.messages.create(
#         thread_id=thread.id,
#         role="user",
#         content=message_input
#     )
#     run = client.beta.threads.runs.create(
#         thread_id=thread.id,
#         assistant_id=config['ASSISTANT_ID']
#     )
#     run = client.beta.threads.runs.retrieve(
#         thread_id=thread.id,
#         run_id=run.id
#     )
#     messages = client.beta.threads.messages.list(
#         thread_id=thread.id
#     )

#     for message in reversed(messages.data):
#         msg_response = message.content[0].text.value

#     return msg_response

def gpt_call(message_input: str):
    user_details = USER
    message_input = message_input + user_details
    gpt_response = client.chat.completions.create(
        model = MODEL_GPT35,
        messages = [
            {"role": "system", "content": INSTRUCTIONS_MARIA},
            {"role": "user", "content": message_input}
        ]
    )
    gpt_response = gpt_response.choices[0].message.content
    gpt_response = gpt_response[0:-1]
    print(gpt_response)

    return {"message": gpt_response}