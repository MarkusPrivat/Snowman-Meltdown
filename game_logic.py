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


def display_game_state(mistakes: int, secret_word: str, guessed_letters: list) -> bool:
    """
    Displays the game state.
    :param mistakes: how many mistakes were made.
    :param secret_word: the secret word that was chosen.
    :param guessed_letters: the guessed letter that was chosen.
    :return: win: the secret_word was guessed
    """
    guessed_word = ""
    guessed = ""
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    print(art.STAGES[mistakes])
    for letter in secret_word:
        if letter in guessed_letters:
            guessed_word += letter + " "
        else:
            guessed_word += "_ "
    print(f"Word: {guessed_word}")
    if len(guessed_letters) > 0:
        for letter in guessed_letters:
            guessed += letter + ", "
        print(f"You already guessed: {guessed[:-2]}")
    print()
    if guessed_word.replace(" ", "") == secret_word:
        return True
    return False


def play_game():
    """
    The game main loop
    :return: None
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    win = False
    print("Welcome to Snowman Meltdown!")
    while mistakes < 4:
        if display_game_state(mistakes, secret_word, guessed_letters):
            win = True
            break
        guess = input("Guess a letter: ").lower()
        guessed_letters.append(guess)
        if not guessed_letters[-1] in secret_word:
            mistakes += 1
    if win:
        print(f"You win! The word was {secret_word}")
    else:
        print(f"You lose! The word was: {secret_word}")


if __name__ == "__main__":
    play_game()