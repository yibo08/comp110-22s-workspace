"""EX03 - Structured Wordle."""
__author__ = "730526118"


def contains_char(searched_word: str, searched_char: str) -> bool:
    """Determines whether the guessing word contains the specified character."""
    assert len(searched_char) == 1
    i: int = 0
    while i < len(searched_word):
        if searched_word[i] == searched_char:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emojified the result with different color boxes."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    i_1: int = 0
    while i_1 < len(secret):
        if guess[i_1] == secret[i_1]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[i_1]) is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        i_1 += 1

    return emoji


def input_guess(length: int) -> str:
    """To test whether the length is correct and ask for a correct one."""
    length_word: str = input(f"Enter a {length} character word:")
    while len(length_word) != length:
        length_word: str = input(f"That wasn't {length} chars! Try again:")
    return length_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 1
    secret_word: str = "codes"
    while turn_number < 7:
        print(f"=== Turn {turn_number}/6 ===")
        guess_word: str = input_guess(5)
        print(emojified(guess_word, secret_word))
        if guess_word == secret_word:
            print(f"You won in {turn_number}/6 turns!")
        turn_number += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
    