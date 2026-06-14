import random

def spin_slot_machine():
    symbols = ["🍒", "🍋", "🍊", "🍉", "⭐"]
    return [random.choice(symbols) for _ in range(3)]
    
def print_slot_machine(row):
    print("-------------")
    print(" | ".join(row))
    print("-------------")

def get_payout(row, bet):
   if row[0] == row[1] == row[2]:
       if row[0] == "⭐":
           return bet * 10
       elif row[0] == "🍒":
           return bet * 2
       elif row[0] == "🍋":
            return bet * 5
       elif row[0] == "🍊":
            return bet * 3
       elif row[0] == "🍉":
            return bet * 4
   return 0
       

def main():
    balance = 100.0
    print("*********************************")
    print("Welcome to the Slot Machine Game!")
    print("You start with a balance of $100.00")
    print("symbols: 🍒, 🍋, 🍊, 🍉, ⭐")
    print("*********************************")

    while balance > 0:
        print(f"Your current balance is: ${balance:.2f}")
        bet = input("enter your bet amount: ")
        
        if not bet.isdigit():
            print("invalid input.Please enter a number.")
            continue
        bet = int(bet)

        if bet <= 0:
            print("Bet amount must be greater than zero.")
            continue

        if bet > balance:
            print("Insufficient balance for this bet.")
            continue
        
        balance -= bet

        row = spin_slot_machine()
        print("Spinning...\n")
        print_slot_machine(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"Congratulations! You won ${payout:.2f}!")
        else:
            print("Sorry, you didn't win this time.")

        balance += payout

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thank you for playing! Goodbye!")
            break

    print(f"Game over. Your final balance is ${balance:.2f}. Thank you for playing!")

if __name__ == "__main__":
    main()