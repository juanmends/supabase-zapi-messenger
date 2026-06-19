import logging
from supabase import create_client

logger = logging.getLogger(__name__)

def buscar_contato(settings):
    try:
        supabase = create_client(settings.supabase_url, settings.supabase_key)
        resposta = supabase.table("users").select("name, number").limit(3).execute()
    except Exception as e:
        logger.error(f"Falha ao buscar contatos: {e}")
        return []
    
    contatos = resposta.data
    logger.info(f"Contatos encontrados: {len(contatos)}")
    return contatos