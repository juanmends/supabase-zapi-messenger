from src.config import Settings
import requests, logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

settings = Settings.le_env()
