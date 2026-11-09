"""A simple number guessing game."""

import random


def main():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed the number in {attempts} tries.")
            break


if __name__ == "__main__":
    main()
