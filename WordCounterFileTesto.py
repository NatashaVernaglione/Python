def conta_parole(percorso_file):
    try:
        with open(percorso_file, "r", encoding="utf-8") as file:
            testo = file.read().lower()

        parole = testo.split()

        frequenze = {}

        for parola in parole:
            frequenze[parola] = frequenze.get(parola, 0) + 1

        top_5 = sorted(frequenze.items(),
                       key=lambda x: x[1],
                       reverse=True)[:5]

        return top_5

    except FileNotFoundError:
        print("Errore: file non trovato.")
        return []


percorso = input("Inserisci il percorso del file: ")

risultato = conta_parole(percorso)

if risultato:
    print("Le 5 parole più frequenti sono:")
    for parola, frequenza in risultato:
        print(f"{parola}: {frequenza}")
