
import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Welcome to the Guessing Game!")
print(f"I'm thinking of a number between {lowest_number} and {highest_number}.")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("the number is out of range.")
            print(f"Please enter a number between {lowest_number} and {highest_number}.")
        elif guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"CORRECT! the answer is {answer}.")
            print(f"You guessed the number in {guesses} guesses.")
            is_running = False
    else:
        print("invalid")
        print(f"Please enter a number between {lowest_number} and {highest_number}.")