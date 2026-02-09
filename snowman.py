import game_logic as gl


def new_round() -> bool:
    """
    Ask the user if they want to play again after a game ends.
    :return: new round
    """
    while True:
        user_input = input("Do you want to play now? (yes/no): ")
        try:
            if not user_input.lower() in ['yes', 'y', 'no', 'n']:
                raise ValueError("Invalid input: must be 'yes' or 'no'.")
            if user_input.lower() in ["yes", "y"]:
                return True
            return False
        except ValueError as error:
            print(error)


def main():
    """
    The main function calls play_game()
    :return: None
    """
    while True:
        gl.play_game()
        if not new_round():
            break


if __name__ == "__main__":
    main()
