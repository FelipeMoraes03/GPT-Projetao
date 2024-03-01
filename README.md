# GPT-Projetao
Modelo do GPT para a cadeira de Projetão (IF683) - 2023.2

### Instalando dependências
```shell
pip install -r requirements.txt
```

### Adicionando key do OpenAI
Para adicionar a key do OpenAI nesse projeto, é necessário que os seguintes passos sejam seguidos:
- Crie um arquivo .env **no diretório base do projeto**
- Copie o arquivo .env.example para o arquivo .env
- Adicione uma key da OpenAI e o ID de um assistant da OpenAI treinado

### Rodando o projeto
```shell
uvicorn server:app --reload
```