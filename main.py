import logging
from src.config import Settings
from src.contacts import buscar_contato
from src.messaging import enviar_mensagem

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

settings = Settings.le_env()

contatos = buscar_contato(settings=settings)

enviadas = 0

for contato in contatos:
    mensagem = f"Olá, {contato['name']} tudo bem com você?"
    if enviar_mensagem(settings=settings, telefone=contato["number"], mensagem=mensagem):
        enviadas += 1

logger.info(f"Mensagens enviadas: {enviadas}")
