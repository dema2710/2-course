from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


password = "123"

hash = context.hash(password)
print(hash)
