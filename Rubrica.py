
contatti = {}

while True:
    print("\n--- RUBRICA CONTATTI ---")
    print("1. Aggiungi contatto")
    print("2. Cerca contatto")
    print("3. Modifica contatto")
    print("4. Elimina contatto")
    print("5. Visualizza contatti")
    print("6. Esci")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        nome = input("Nome: ")
        telefono = input("Telefono: ")
        contatti[nome] = telefono
        print("Contatto aggiunto.")

    elif scelta == "2":
        nome = input("Nome da cercare: ")
        if nome in contatti:
            print(f"{nome}: {contatti[nome]}")
        else:
            print("Contatto non trovato.")

    elif scelta == "3":
        nome = input("Nome del contatto da modificare: ")
        if nome in contatti:
            nuovo_numero = input("Nuovo numero: ")
            contatti[nome] = nuovo_numero
            print("Contatto modificato.")
        else:
            print("Contatto non trovato.")

    elif scelta == "4":
        nome = input("Nome del contatto da eliminare: ")
        if nome in contatti:
            del contatti[nome]
            print("Contatto eliminato.")
        else:
            print("Contatto non trovato.")

    elif scelta == "5":
        if contatti:
            print("\nElenco contatti:")
            for nome, telefono in contatti.items():
                print(f"{nome}: {telefono}")
        else:
            print("Nessun contatto presente.")

    elif scelta == "6":
        print("Programma terminato.")
        break

    else:
        print("Scelta non valida.")
        
#scelta nuova operazione o no     
    while True:
        continua = input("\nVuoi effettuare un'altra operazione? (y/n): ").lower()
        
        if continua == "y":
            break  # torna al menu principale
        
        elif continua == "n":
            print("Programma terminato.")
            exit()
        
        else:
            print("Inserisci solo y o n.")
