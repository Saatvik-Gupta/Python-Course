import random

# List of words
words = ["python", "computer", "programming", "algorithm", "database"]

# Select a random word
word = random.choice(words)

# Hangman stages
hangman = [
    """
     +---+
     |   |
         |
         |
        ===
    """,
    """
     +---+
     |   |
     O   |
         |
        ===
    """,
    """
     +---+
     |   |
     O   |
     |   |
        ===
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
        ===
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
        ===
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
        ===
    """
]

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("===== HANGMAN GAME =====")

while wrong_guesses < max_wrong_guesses:

    # Display the hangman
    print(hangman[wrong_guesses])

    # Display the word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations!")
        print("You guessed the word:", word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    # Store guessed letter
    guessed_letters.append(guess)

    # Check whether guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    # Game over
    print(hangman[wrong_guesses])
    print("\nGAME OVER!")
    print("The correct word was:", word)