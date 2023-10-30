import random

def generate_random_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)

def get_user_guess():
    """Prompts the user for a guess."""
    guess = int(input("Enter your guess: "))
    return guess

def check_guess(guess, secret_number):
    """Checks if the user's guess is correct.

    Args:
      guess: The user's guess.
      secret_number: The secret number.

    Returns:
      A string indicating whether the guess is too high, too low, or correct.
    """

    if guess > secret_number:
        return "Too high."
    elif guess < secret_number:
        return "Too low."
    else:
        return "Correct!"

def play_game():
    """Plays the guessing game."""

    secret_number = generate_random_number()

    num_guesses = 0
    while num_guesses < 5:
        guess = get_user_guess()
        result = check_guess(guess, secret_number)

        print(result)

        if result == "Correct!":
            break

        num_guesses += 1

    if num_guesses == 5:
        print("You ran out of guesses. The secret number was {}.".format(secret_number))
    else:
        print("You guessed correctly in {} guesses!".format(num_guesses))

if __name__ == "__main__":
    play_game()
