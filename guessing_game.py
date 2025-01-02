#! /usr/bin/python3

import random

# TO DO
# Handle input from user
# Define a function that handles if the user guess the random number correctly


def welcome_msg() -> int:
    """Displays the welcome message and prompts the user to select a difficulty level.

    Returns:
        int: The user's choice (1 for Easy, 2 for Medium, 3 for Hard).
    """
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a Number between 1 and 100")
    print("")
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print("")
    print("")

    while True:
        choice = input("Enter your choice: ")
        print()
        try:
            choice = int(choice)
            if choice in [1, 2, 3]:
                return choice
            else:
                raise ValueError
        except ValueError:
            print("choice should be a number between 1, 2, or 3")
            print()
            continue


def random_num() -> int:
    """This select a random number between 1 to 100

    returns:
        int: A random number between 1 to 100
    """
    return random.randint(1, 100)


def state_difficulty(level: str) -> None:
    """Displays the user's selected difficulty level.

    Args:
        level (str): The user's difficulty level (e.g., 'Easy', 'Medium', 'Hard').
    """
    print(f"Great! You have selected the {level} difficulty level.")
    print("Let's start the game!")
    print()


def chance_manager(choice: int) -> int:
    """Converts the user's difficulty choice into the corresponding number of chances
    and displays the remaining chances.

    Args:
        choice (int): The user's difficulty choice (1 for Easy, 2 for Medium, 3 for Hard).

    returns:
        int: The number of chances allocated based on the user's choice.
    """

    match choice:
        case 1:
            chance = 10
            state_difficulty("Easy")
        case 2:
            chance = 5
            state_difficulty("Medium")
        case 3:
            chance = 3
            state_difficulty("Hard")
    print(f"You have {chance} chances to guess the correct number.")
    return chance


def check_user_guess(chances_left: int, random_val: int) -> None:
    if chances_left == 0:
        print("Sorry, you've run out of chances! Better luck next time.")
        print()
        return

    guess = input("Enter your guess: ")
    try:
        guess = int(guess)
        if 1 <= guess <= 100:
            if random_val < guess:
                print(f"Incorrect! The number is less than {guess}")
                print()
            elif random_val > guess:
                print(f"Incorrect! The number is greater than {guess}")
                print()
            else:
                print(
                    f"Congratulations! You guessed the correct number with {chances_left} attempts remaining!"
                )
                print()
                return
        else:
            raise ValueError
    except ValueError:
        print("Your guess should be a number and should be between 1 to 100")
        print()

    print(f"You have {chances_left - 1} chances left.")
    print()
    check_user_guess(chances_left - 1, random_val)


def main():
    chance = chance_manager(welcome_msg())
    random_val = random_num()
    check_user_guess(chance, random_val)


# if "__name__" == "__main__":
#     main()
main()
# print(chance_manager(welcome_msg()))
# while True:
#     choice = welcome_msg()
