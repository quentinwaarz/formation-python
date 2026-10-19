import random
secret = random.randint(1, 100)

def demander_nombre():
    while True:
        try:
            reponse = input("Ton nombre ? ")
            nombre = int(reponse)
            return nombre
        
        except ValueError:
            print("Entre un nombre entier !")

choix = 0
essais = 0
            
while choix != secret:
    
    choix = demander_nombre()   
    essais = essais + 1

    if choix < secret:
        print ("Trop petit")
    elif choix == secret:
        print ("Gagné !")
    else:
        print ("Trop grand")
        
    
if essais == 1:     
    print ("Gagné en", essais ,"essai !")
else:
    print ("Gagné en", essais ,"essais !")