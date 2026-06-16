import secrets
import string

# Definiamo i caratteri da usare: lettere, numeri e simboli
caratteri = string.ascii_letters + string.digits + string.punctuation

# Generiamo una password lunga 16 caratteri
lunghezza = 16
password = "".join(secrets.choice(caratteri) for i in range(lunghezza))

print(password)
