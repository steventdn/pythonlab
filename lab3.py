import random

def play_guessing_game():
    random_number = random.randint(1, 100)
    num_of_guesses = 0

    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        num_of_guesses += 1

        if user_guess < random_number:
            print("Too low, try again.")
        elif user_guess > random_number:
            print("Too high, try again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} correctly!")
            print(f"Number of guesses: {num_of_guesses}")
            break

if __name__ == '__main__':
    play_guessing_game()
