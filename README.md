# Number Guessing Game 🎲

A CLI-based interactive number guessing game where the computer randomly selects a number between 1 and 100, and the user tries to guess it within a limited number of attempts.

## Features ✨

- Randomly generated number between 1 and 100.
- Multiple difficulty levels:
  - **Easy**: 10 chances
  - **Medium**: 5 chances
  - **Hard**: 3 chances
- Provides feedback on each guess, indicating whether the target number is greater or less.
- Displays a congratulatory message when the user guesses correctly.
- Tracks the remaining attempts and ends the game when the user runs out of chances.
- Simple and user-friendly command-line interface.

## How It Works ⚙️

1. The game starts with a welcome message and rules.
2. Users select a difficulty level:
   - **Easy**: 10 attempts
   - **Medium**: 5 attempts
   - **Hard**: 3 attempts
3. The computer randomly selects a number between 1 and 100.
4. Users input their guesses:
   - If the guess is correct, the game ends with a success message.
   - If incorrect, the game provides hints (greater or less) and decrements the remaining attempts.
5. The game ends when:
   - The user guesses the correct number.
   - The user runs out of attempts.

## Example Run 🖥️

```text
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2

Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

Enter your guess: 35
Incorrect! The number is less than 35.

Enter your guess: 30
Congratulations! You guessed the correct number in 4 attempts!
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hakeemyusuff/Number_guessing_game.git
cd Number_guessing_game
```

2. Make executable and run the game:

```bash
chmod +x guessing_game.py
./guessing_game.py
```

## This project is part the [[roadmap.sh](https://roadmap.sh/projects/number-guessing-game)] Backend projects
