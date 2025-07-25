import secrets
from argon2 import PasswordHasher

clave = secrets.token_urlsafe(64)

print("Hash JWT:\n" + clave)

ph = PasswordHasher()

hash = ph.hash("abcd")

print("Contraseña hasheada Argon:" + str(len(hash)) + "\n" + hash)

ph = PasswordHasher()

try:
    ph.verify("$argon2id$v=19$m=65536,t=3,p=4$e8FwjlKtpUUM7nGw5CgeXw$tcPU54QVt2Xh3w+0EvCUFyoEOGb3aRwShCkTLdo8BT0", "abcd")
    print("La contra es correcta")
except:
    print("La contra no es correcta")