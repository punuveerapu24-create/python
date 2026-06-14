import random

fruits = [
    "apple", "banana", "orange", "strawberry", "grape", 
    "mango", "pineapple", "peach", "plum", "cherry", 
    "kiwi", "watermelon", "pear", "lemon", "lime", 
    "blueberry", "raspberry", "blackberry", "pomegranate", "papaya", 
    "cantaloupe", "honeydew", "fig", "date", "avocado", 
    "guava", "lychee", "tangerine"
]


hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" O ",
                  "   ",
                  "   "),
               2:(" O ",
                  " | ",
                  "   "),
               3:(" O ",
                  "/| ",
                  "   "),
               4:(" O ",
                  "/|\\",
                  "   "),
               5:(" O ",
                  "/|\\",
                  "/  "),
               6:(" O ",
                  "/|\\",
                  "/ \\")}

def display_man(wrong_guess):
    print("--------")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("--------")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(fruits)
    hint = ["_"] * len(answer)
    wrong_guess = 0
    guessed_letter = set()
    is_running = True

    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letter:
            print(f"{guess} has already been guessed")
            continue

        guessed_letter.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guess += 1

        if "_" not in hint:
            display_man(wrong_guess)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guess >= len(hangman_art) - 1:
            display_man(wrong_guess)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()
