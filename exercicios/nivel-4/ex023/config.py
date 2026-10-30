import os
from dotenv import load_dotenv

load_dotenv()

URL_DATABASE = os.getenv("URL_DATABASE")
TEST_URL_DATABASE = os.getenv("TEST_URL_DATABASE")

if not URL_DATABASE:
    raise RuntimeError("URL_DATABASE não configurada no .env")

if not TEST_URL_DATABASE:
    raise RuntimeError("TEST_URL_DATABASE não configurada")