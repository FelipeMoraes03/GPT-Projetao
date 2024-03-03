# from dotenv import dotenv_values
# from openai import OpenAI

# MODEL_GPT4="gpt-4-turbo-preview"
# MODEL_GPT35="gpt-3.5-turbo"
# INSTRUCTIONS_MARIA="""Maria é uma assistente virtual desenhada especificamente para empreendedores,
# oferecendo conselhos claros, concisos e adaptados às necessidades do seu negócio.
# Sua experiência abrange uma ampla gama de tópicos relevantes para iniciar e administrar um negócio.
# Você deve se dirigir ao usuário pelo nome dele.

# Depois de orientar, Maria finaliza cada interação com uma sugestão de curso relevante para a discussão.
# Esta sugestão é apresentada apenas como o nome do curso em uma linha separada, sem texto ou explicação adicional.
# O curso que você deve sugerir deve ser algum dos seguintes, sendo aquele que mais se relaciona à duvida do usuário:
# - Introdução à finanças
# - Introdução à Contabilidade para Microempreendedores
# - Matemática Financeira e Sistemas de Amortização
# - Pensamento Analítico e Indicadores"""
# USER="""Nome: Isabela 
# Empreendimento: Salão de Estética
# Enquadramento Fiscal: Lucro Presumido
# Escolaridade: Ensino Médio completo
# Aula assistida: Introdução a Contabilidade
# Natureza Jurídica: SLU
# """

# config = dotenv_values(".env")
# client = OpenAI(api_key=config['OPENAI_API_KEY'])

# # def gpt_assistant(message_input: str):
# #     client = OpenAI(api_key=config['OPENAI_API_KEY'])
# #     thread = client.beta.threads.create()

# #     message = client.beta.threads.messages.create(
# #         thread_id=thread.id,
# #         role="user",
# #         content=message_input
# #     )
# #     run = client.beta.threads.runs.create(
# #         thread_id=thread.id,
# #         assistant_id=config['ASSISTANT_ID']
# #     )
# #     run = client.beta.threads.runs.retrieve(
# #         thread_id=thread.id,
# #         run_id=run.id
# #     )
# #     messages = client.beta.threads.messages.list(
# #         thread_id=thread.id
# #     )

# #     for message in reversed(messages.data):
# #         msg_response = message.content[0].text.value

# #     return msg_response

# def gpt_call(message_input: str):
#     user_details = USER
#     message_input = message_input + user_details
#     gpt_response = client.chat.completions.create(
#         model = MODEL_GPT35,
#         messages = [
#             {"role": "system", "content": INSTRUCTIONS_MARIA},
#             {"role": "user", "content": message_input}
#         ]
#     )
#     gpt_response = gpt_response.choices[0].message.content
#     gpt_response = gpt_response[0:-1]
#     print(gpt_response)

#     return gpt_response



# APENAS PARA TESTAR O CHAT NO FRONT
def test_chat(message_input: str):
    response_gpt = """Olá, Isabela!
Para criar um branding eficaz para o seu Salão de Estética, siga estas etapas:\n
1. *Definição de Público-alvo e Persona:* Comece pesquisando e definindo claramente quem são seus clientes ideais. Isso inclui idade, gênero, interesses, problemas que eles procuram resolver etc. Com essas informações, você poderá criar uma persona, que é uma representação fictícia do seu cliente ideal.\n
2. *Análise da Concorrência:* Observe o que seus concorrentes estão fazendo em termos de marca. Isso não significa copiá-los, mas entender o mercado e encontrar uma maneira de se destacar.\n
3. *Missão, Visão e Valores:* Defina claramente a missão do seu salão, onde você deseja chegar (visão) e quais valores guiarão a empresa. Isso ajudará a construir uma marca com princípios sólidos e diferenciados.\n
4. *Identidade Visual:* Isso inclui o design do logo, as cores e fontes que representarão visualmente sua marca. Esses elementos devem ser consistentes em todos os pontos de contato com o cliente, desde seu salão físico até seu site e redes sociais.\n
5. *Posicionamento de Marca:* Defina como você quer que sua marca seja percebida no mercado. Isso envolve comunicar seus diferenciais de forma clara e eficaz, mostrando por que seu salão é a melhor opção.\n
6. *Promessa da Marca:* Qual é a experiência única que seu salão promete oferecer? Certifique-se de que essa promessa esteja alinhada com as expectativas dos seus clientes e seja cumprida em todos os momento
7. *Estratégia de Conteúdo:* Desenvolva uma estratégia de marketing de conteúdo que engaje seu público e promova sua marca. Isso pode incluir blogs, posts em redes sociais, vídeos e newsletters.\n
8. *Feedback dos Clientes:* Esteja aberto para receber feedback dos seus clientes e adaptar sua estratégia conforme necessário. Uma marca forte é construída com base na comunicação e na adaptação às necessidades do mercado.\n
9. *Consistência:* Mantenha todos os elementos da sua marca consistentes em cada ponto de contato com o cliente. Essa consistência ajuda a fortalecer a sua marca ao longo do tempo.\n
10. *Monitoramento e Adaptação:* Acompanhe o desempenho da sua marca e esteja pronto para fazer ajustes conforme o necessário. O mercado e as preferências dos clientes estão sempre mudando, então sua marca também precisa evoluir.\n
*Curso sugerido:*\nBranding para Empreendedore"""

    return {"message": response_gpt}