import requests, logging

logger = logging.getLogger(__name__)

def enviar_mensagem(settings, telefone, mensagem):

    url = f"https://api.z-api.io/instances/{settings.zapi_instance_id}/token/{settings.zapi_token}/send-text"
    headers = {"Client-Token": settings.zapi_client_token}
    body = {"phone":telefone, "message":mensagem}

    try:
        resposta = requests.post(url,headers=headers,json=body)
    except requests.exceptions.RequestException as e:
        logger.error(f"Falha de rede ao enviar: {e}")
        return False

    if resposta.status_code == 200:
        logger.info(f"Mensagem enviada com sucesso para {telefone}")
        return True
    else:
        logger.error(f"Falha ao enviar mensagem para {telefone}: {resposta.text}")
        return False