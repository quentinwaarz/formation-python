# --- Exercice 1 : prenom ---
prenom = "Quentin"

print(len(prenom))
print(prenom[0])
print(prenom[-1])
print(prenom.upper())

# --- Exercice 2 : phrase ---

phrase = "  le python, c'est cool  "
mots = phrase.strip().split()
for mot in mots:
    print(mot)

print(phrase.strip().split())

# --- Exercice 2 : programme ---

prenom = input("Ton prenom ? ")
n = len(prenom)

print(f"Bonjour {prenom} ! Ton prénom contient {n} lettres.")