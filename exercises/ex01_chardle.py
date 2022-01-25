"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730526118"


word: str = input("Enter a 5-character word:")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()


char: str = input("Enter a single character:")
if len(char) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + char + " in " + word)

inst: int = 0

if char == word[0]:
    print(char + " found at index 0")
    inst = inst + 1

if char == word[1]:
    print(char + " found at index 1")
    inst = inst + 1

if char == word[2]:
    print(char + " found at index 2")
    inst = inst + 1

if char == word[3]:
    print(char + " found at index 3")    
    inst = inst + 1

if char == word[4]:
    print(char + " found at index 4")
    inst = inst + 1

if inst > 0:
    if inst == 1:
        print(str(inst) + " instance for " + char + " found in " + word)
    if inst > 1:
        print(str(inst) + " instances for " + char + " found in " + word)
else:
    print("No instances of " + char + " found in " + word)