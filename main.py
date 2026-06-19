from src.config import Settings
from src.contacts import buscar_contato
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

settings = Settings.le_env()

contatos = buscar_contato(settings=settings)

for contato in contatos:
    print(contato["name"], contato["number"])