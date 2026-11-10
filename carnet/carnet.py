while True :
    tache = input("Nouvelle tâche ? ")
    if tache == "q":
        break
    with open("taches.txt", "a", encoding="utf-8") as f:
        f.write(f"{tache}\n")
    

with open("taches.txt", "r", encoding="utf-8") as f:
        numero = 0
        for ligne in f:
            numero = numero + 1
            print(f"{numero}. {ligne.strip()}")
    