#2. Numeri primi in un range
#Scrivi una funzione numeri_primi(inizio, fine) che restituisce una lista di tutti i numeri primi compresi tra inizio e fine.

# 1. Contatore di vocali
def numeri_primi(inizio, fine):

# Funzione interna che verifica se un singolo numero è primo
    def is_primo(n):
        if n < 2:
            return False  # 0 e 1 non sono primi per definizione
    
# Funzione interna che verifica se un singolo numero è primo
        if n % 2 == 0:
            return False
 
        return True
 
# List comprehension: filtra i numeri nel range che superano il test is_primo
    return [n for n in range(inizio, fine + 1) if is_primo(n)]

n = int(input("Inserisci un numero: "))
if n in numeri_primi(n, n): # cerca tutti i primi da 1 fino a n
  print("Il numero è primo")
else:
  print("Il numero non è primo")
