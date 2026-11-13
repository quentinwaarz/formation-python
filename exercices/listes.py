# --- Exercice 1  ---
notes = [12, 15, 8, 10, 17]
somme = 0
for note in notes: 
    somme = somme + note

print(notes[0])       
print(len(notes))      
print(notes[-1])
print(somme)
print(somme / len(notes))

# --- Exercice 2 ---
livre = {"titre": "Livre Cool", "auteur": "ELektra", "pages": 30}

print(livre["titre"]) 
print(livre["titre"], "de", livre["auteur"])    
livre["pages"] = 31          
livre["annee"] = 2038   
print(livre)