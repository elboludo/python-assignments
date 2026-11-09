"""Guess a randomly chosen number within a user-selected level."""

import random


def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
        except ValueError:
            pass


def main():
    level = get_positive_integer("Level: ")
    answer = random.randint(1, level)

    while True:
        guess = get_positive_integer("Guess: ")

        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
