import re

pwd = input("Inserisci una password: ")

def valida_password(pwd):
    
    try:
        if not isinstance(pwd, str):
            raise TypeError("La password deve essere una stringa.")

        if len(pwd) < 8:
            return False

        if not re.search(r"[A-Z]", pwd):  # almeno una maiuscola
            return False

        if not re.search(r"[a-z]", pwd):  # almeno una minuscola
            return False

        if not re.search(r"\d", pwd):     # almeno un numero
            return False

        return True

    except TypeError as errore:
        print("Errore:", errore)
        return False
        
# Test della funzione
if valida_password(pwd):
    print("Password valida")
else:
    print("Password non valida")  
        
        
