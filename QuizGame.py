
questions = ("What is the capital of France?",
             "What is the largest planet in our solar system?",
             "What is the chemical symbol for gold?",
             "Who painted the Mona Lisa?")

options = (("A. London", "B. Berlin", "C. Paris", "D. Madrid"),
           ("A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"),
           ("A. Go", "B. Au", "C. Ag", "D. Fe"),
           ("A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"))

answers = ("C", "C", "B", "C")

guesses = []

score = 0

question_number = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_number]} was the correct answer.")
    question_number += 1

print("------------RESULTS-------------")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")