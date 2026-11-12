def ajouter():  
    while True :
        tache = input("Nouvelle tâche ? ").strip()
        if tache == "q":
            break
        elif tache == "":
            continue
        with open("taches.txt", "a", encoding="utf-8") as f:
            f.write(f"{tache}\n")

def afficher():    
    try:
        with open("taches.txt", "r", encoding="utf-8") as f:
            numero = 0
            for ligne in f:
                numero = numero + 1
                print(f"{numero}. {ligne.strip()}")
    except FileNotFoundError:
        print("Aucune tâche pour l'instant.")

def supprimer():
    try:
        with open("taches.txt", "r", encoding="utf-8") as f:
            taches = f.readlines()
    except FileNotFoundError:
        print("Aucune tâche à supprimer.")
        return
    try :
        numero = int(input("Numéro à supprimer ? "))
    except ValueError :
        print("Entre un nombre.")
        return
    if 1 <= numero <= len(taches) :
        taches.pop(numero - 1)
        with open("taches.txt", "w", encoding="utf-8") as f:
            for tache in taches:
                f.write(tache)
    else: print ("Numéro invalide.")

while True:
    print("1. Ajouter")
    print("2. Afficher")
    print("3. Supprimer")
    print("4. Quitter")
    choix = input("Ton choix ? ")

    if choix == "1":
        ajouter()
    elif choix == "2":
        afficher()
    elif choix == "3":
        supprimer()
    elif choix == "4":
        break
    else:
        print("Choix invalide.")