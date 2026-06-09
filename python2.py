
secret_password = "open sesame"


user_guess = ""

print("The treasure chest is locked!")


while user_guess != secret_password:
    
    
    user_guess = input("Enter the password to unlock: ")
    
    
    if user_guess != secret_password:
        print("Wrong password! The chest remains locked. Try again")


print(" Success! The treasure chest is open!")