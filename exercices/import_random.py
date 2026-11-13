import random
secret = random.randint(1, 100)

nombre = 0
essais = 0
while nombre != secret:
    try:
        reponse = input("Ton nombre ? ")
        nombre = int(reponse)
        essais = essais + 1

    except ValueError:
        print("Entre un nombre entier !")
        continue
    
    if nombre < secret:
        print ("Trop petit")
    elif nombre == secret:
        print ("Gagné !")
    else:
        print ("Trop grand")
        
    
if essais == 1:     
    print ("Gagné en", essais ,"essai !")
else:
    print ("Gagné en", essais ,"essais !")