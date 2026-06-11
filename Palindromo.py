#4. Palindromo
#Scrivi una funzione e_palindromo(frase) che verifica se una frase è palindroma, ignorando spazi, maiuscole/minuscole e punteggiatura (es. "I topi non avevano nipoti").

#re è il modulo della libreria standard di Python per le espressioni regolari
import re

def e_palindromo(frase):
    # 1. minuscolo e assegna il risultato
    pulita = frase.lower()
    
    # 2. rimuove tutto tranne le lettere
    pulita = "".join(c for c in pulita if c.isalpha())
    
    # 3. confronta con l'inverso
    return pulita == pulita[::-1]

# input() fuori dalla funzione
frase = input("Inserisci un testo: ")
if e_palindromo(frase):
    print("Il testo è palindromo")
else:
    print("Il testo non è palindromo")
