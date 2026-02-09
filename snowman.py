import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

def get_random_word():
    """
    Selects a random word from the list.
    :return: a random word from the list.
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes: int, secret_word: str, guessed_letters: list):
    """
    Displays the game state.
    :param mistakes: how many mistakes were made.
    :param secret_word: the secret word that was chosen.
    :param guessed_letters: the guessed letter that was chosen.
    :return: 
    """
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    print(STAGES[mistakes])
    print(f"Word: {"_" * len(secret_word)}")
    print(f"You guessed: {guessed_letters}")


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
    display_game_state(mistakes, secret_word, guessed_letters)
    guessed_letters.append(input("Guess a letter: ").lower())



if __name__ == "__main__":
    play_game()