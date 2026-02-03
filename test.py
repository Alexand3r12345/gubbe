
import random

ordlista = ["bord", "målare", "tavla"]
word = random.choice(ordlista).lower()

play_word = list(word)
guessed_word = ["_"] * len(word)
used_letters = []

fel = 0
max_fel = 6

print("Välkommen till hänge gubbe")
print("Ordet har", len(play_word), "bokstäver")


while fel < max_fel and "_" in guessed_word:
    print("\ordet:", "".join(guessed_word))
    print("gissade bokstäver:", ", ".join(used_letters))


    try:
        guess = input("Gissa en bokstav").lower()

        if len(guess) != 1:
            raise ValueError("du måste gissa en bokstav")
     
        if guess in used_letters:
            raise ValueError("du har redan gissat den bokstaven")
    
        used_letters.append(guess)

        if guess in play_word:
             for i, letter in enumerate(play_word):
                  if letter == guess:
                    guessed_word[i] = guess
                    print("rätt")
        else:
            fel += 1
            print("fel, antal fel:", fel, "av", max_fel)
        
    except ValueError as f:
            print("fel", f)
        

if "_" not in guessed_word:
    print("yay du vann ordet var:", word)
else:
    print("tyvärr du förlorade ordet var:", word)


 



