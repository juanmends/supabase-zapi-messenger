# Envio de mensagens via Z-API

Projeto em Python que lê contatos cadastrados no Supabase e envia uma mensagem personalizada via Z-API.

Desafio técnico b2bflow.

## Setup da tabela
 
No Supabase, crie a tabela "users" com as colunas "id", "name" e "number", quando fui testar também coloquei "created_at" mas essa coluna é opcional.

obs: id é um int8, name e number são text. 
 
Insira os contatos de teste. O número deve estar no formato internacional (DDI + DDD + número), por exemplo 5521999999999
 
exemplos de usuarios:
    ("Fulano", "5521999999999"),
    ("Ciclano", "5521988888888"),
    ("Beltrano", "5521977777777");
 
O Supabase ativa o Row Level Security (RLS) por padrão. Para que o script consiga ler a tabela, crie uma policy de leitura (SELECT) para "users" ou use a chave "service_role" no .env

## Configuração
 
Crie um .env com as seguintes informações:
```
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=
```

Atenção: A "SUPABASE_URL" deve ser apenas a URL base do projeto (https://xxxx.supabase.co), sem "/rest/v1" no final

## Como rodar
 
Instale as dependências e execute:
 
```
pip install -r requirements.txt
python main.py
```