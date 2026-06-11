#5. Statistiche su una lista
#Data una lista di numeri inseriti dall'utente (separati da virgola, da input()), calcola media, massimo, minimo e mediana. Gestisci il caso in cui l'utente inserisca valori non numerici.

testo = input("Inserisci numeri separati da virgola: ")

# converte la stringa in lista, gestendo valori non numerici
numeri = []
for elemento in testo.split(","):
    try:
        numeri.append(float(elemento.strip()))
    except ValueError:
        print(f"  '{elemento.strip()}' non è un numero, ignorato")

if len(numeri) == 0:
    print("Nessun numero valido inserito.")
else:
    numeri.sort()
    media = sum(numeri) / len(numeri)
    massimo = max(numeri)
    minimo = min(numeri)

    # mediana
    n = len(numeri)
    if n % 2 == 1:
        mediana = numeri[n // 2]
    else:
        mediana = (numeri[n // 2 - 1] + numeri[n // 2]) / 2

    print(f"\nMedia:   {media}")
    print(f"Massimo: {massimo}")
    print(f"Minimo:  {minimo}")
    print(f"Mediana: {mediana}")
