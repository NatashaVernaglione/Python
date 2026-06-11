#1. Contatore di vocali
#Scrivi una funzione conta_vocali(testo) che restituisce un dizionario con il conteggio di ogni vocale presente in una stringa (case insensitive).

# 1. Contatore di vocali
def conta_vocali(testo):
    vocali = "aeiouè"
    #Crea un dizionario con tutte le vocali inizializzate a 0
    conteggio = {v: 0 for v in vocali}
    
    #Scorre ogni carattere del testo (convertito in minuscolo con .lower())
    for carattere in testo.lower():
        if carattere in vocali:
          #Se il carattere è una vocale, incrementa il contatore corrispondente
            conteggio[carattere] += 1
    
    return conteggio

testo = input("Inserisci un testo: ")
risultato = conta_vocali(testo)

print(f"Totale vocali: {sum(risultato.values())}")
