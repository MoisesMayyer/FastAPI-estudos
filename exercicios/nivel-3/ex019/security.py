from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/token")
