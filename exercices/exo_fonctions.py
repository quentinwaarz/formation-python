# --- Exercice 1 : ressenti ---
def ressenti(temperature):
    if temperature < 15:
        return "Il fait froid"
    elif temperature <= 25:
        return "Il fait bon"
    else:
        return "Il fait chaud"
print(ressenti(14))
print(ressenti(15))
print(ressenti(25))
print(ressenti(26))

# --- Exercice 2 : aire_rectangle ----
def aire_rectangle(longueur, largeur):
    return longueur * largeur
print(aire_rectangle(5,3))