tassi_cambio = {
    "USD": 1.08,
    "GBP": 0.85,
    "JPY": 170.50
}

def converti(importo, valuta):
    try:
        return importo * tassi_cambio[valuta]
    except KeyError:
        print("Valuta non disponibile.")
        return None

importo = float(input("Inserisci l'importo in EUR: "))
valuta = input("Inserisci la valuta (USD, GBP, JPY): ").upper()

risultato = converti(importo, valuta)

if risultato is not None:
    print(f"{importo} EUR = {risultato:.2f} {valuta}") 
