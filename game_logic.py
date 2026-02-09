import random

import ascii_art as art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """
    Selects a random word from the list.
    :return: a random word from the list.
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes: int, secret_word: str, guessed_letters: list) -> None:
    """
    Displays the game state.
    :param mistakes: how many mistakes were made.
    :param secret_word: the secret word that was chosen.
    :param guessed_letters: the guessed letter that was chosen.
    :return: mistake: player guessed a wrong letter
    """
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    print(art.STAGES[mistakes])
    print("Word: ", end="")
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end="")
        else:
            print("_", end="")
    print()
    if len(guessed_letters) > 0:
        print(f"You guessed: {guessed_letters[-1]}")
    return

def play_game():
    """
    The game main loop
    :return: None
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")

    # TODO: Build your game loop here.
    while mistakes < 4:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        guessed_letters.append(guess)
        if not guessed_letters[-1] in secret_word:
            mistakes += 1
        print(mistakes) # for testing, later remove this line



if __name__ == "__main__":
    play_game()