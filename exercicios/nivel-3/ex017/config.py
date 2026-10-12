import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY2")
ALGORITHM = os.getenv("ALGORITHM2", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES2", "30"))

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY não configurada no .env")