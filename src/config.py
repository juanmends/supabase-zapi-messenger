#único arquivo que sabe da existência do .env
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

def validacao(nome_variavel):
    variavel = os.getenv(nome_variavel)
    if variavel:
        return variavel
    else:
        raise ValueError(f"Variável de ambiente '{nome_variavel}' não está definida. Confira seu .env.")

@dataclass
class Settings:
    supabase_url: str
    supabase_key: str
    zapi_instance_id: str
    zapi_token: str
    zapi_client_token: str

    @classmethod
    def le_env(cls):
        url = validacao("SUPABASE_URL")
        key = validacao("SUPABASE_KEY")
        z_id = validacao("ZAPI_INSTANCE_ID")
        z_token = validacao("ZAPI_TOKEN")
        z_c_token = validacao("ZAPI_CLIENT_TOKEN")
        
        return cls(supabase_url=url, supabase_key=key, zapi_instance_id=z_id, zapi_token=z_token, zapi_client_token=z_c_token)