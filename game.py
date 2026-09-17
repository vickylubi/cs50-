import random


def get_level():
    #Ask the user for a level until they enter a positive integer.
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass


def get_guess():
    #Ask the user for a guess until they enter a positive integer.
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass


def main():
    # Ask for a level that is a positive int (n)
    level = get_level()

    # Generate a random number between 1 and n, inclusive
    number = random.randint(1, level)

    # Keep asking for guesses until the user gets it right
    while True:
        guess = get_guess()
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()