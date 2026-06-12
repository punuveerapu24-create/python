def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")
def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"${amount:.2f} deposited successfully.")
    else:
        print("Invalid amount. Please enter a positive number.")
    return balance
def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds. Withdrawal failed.")
    elif amount <= 0:
        print("Invalid amount. Please enter a positive number.")
    else:
        balance -= amount
        print(f"${amount:.2f} withdrawn successfully.")
    return balance
def main():
    balance = 0.0
    while True:
        print("\nWelcome to the Banking System")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Please select an option (1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()