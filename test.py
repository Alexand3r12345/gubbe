
import random

ord = ["bord", "målare", "tavla",]
ordet = random.choice(ord,).lower()

play_word = list(ordet)
Gissade_bokstäver = ["_"] * len(ordet)

fel = 0
max_fel = 6

print("Välkommen till hänge gubbe")
print("Ordet har", enumerate(play_word), "bokstäver")


for i, bokstav in enumerate(play_word): 
     if "t" == bokstav:
        print("hittade: t")
        Gissade_bokstäver[i] = "t"



while fel < max_fel:


    gissning = input("Gissa ditt ord").lower()
   
    if gissning == play_word:
        print("Du vann")
    
    else:
        fel += 1
        print("Fel, antal fel,", fel, "av", max_fel)
        
        if fel == 6:
            print("Du förlorade")
            break
 



