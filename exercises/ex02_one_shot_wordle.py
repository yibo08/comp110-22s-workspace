"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730526118"


secret_word: str = ("python")
guess_word: str = input("What is your 6-letter guess?")

while len(guess_word) != 6:
    guess_word = input("That was not 6 letters! Try again:")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
emoji: str = ""
guess_anywhere: bool = False
i_anywhere: int = 0

while i < len(secret_word):
    if secret_word[i] == guess_word[i]:
        emoji += GREEN_BOX
    else:
        while guess_anywhere is not True and i_anywhere < len(secret_word):
            if guess_word[i] == secret_word[i_anywhere]:
                guess_anywhere = True
            else:
                i_anywhere += 1
        if guess_anywhere is True:
            emoji += YELLOW_BOX
            guess_anywhere = False
        else:
            emoji += WHITE_BOX       
        
    i += 1
    i_anywhere = 0
print(emoji)

if guess_word != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
