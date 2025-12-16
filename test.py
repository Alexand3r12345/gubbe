
import random

ord4 = ["bord", "målare", "tavla",]

ordet = random.choice(ord4,).lower()
poäng = 0
max_fel = 6

Gissade_bokstäver = []

print("Välkommen till hänge gubbe")
print("Ordet har", len(ordet), "bokstäver")


while poäng < max_fel:
    display=""
    for bokstav in ordet:
        if bokstav in Gissade_bokstäver:
            display += bokstav
        else:
            display += "_"
    print(display)

    gissning = input("Gissa ditt ord").lower()
   
    if gissning == ordet:
        print("Du vann")
    
    else:
        poäng += 1
        print("Fel, antal fel,", poäng, "av", max_fel)
        
        if poäng == 6:
            print("Du förlorade")
            break
    if all(bokstav in Gissade_bokstäver for bokstav in ordet):
        print("Grattis! Du gissade ordet:", ordet)
        break



