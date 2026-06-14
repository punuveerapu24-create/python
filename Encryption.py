import random
import string

characters = string.ascii_letters + string.digits + string.punctuation + " "
characters = list(characters)

key = characters.copy()
random.shuffle(key)

# Encrypt
plain_text = input("Enter a message to encrypt: ")
crypted_text = ""

for letter in plain_text:
    index = characters.index(letter)
    crypted_text += key[index]

print (f"orginal message: {plain_text}")
print (f"encrypted message: {crypted_text}")

# Decrypt
crypted_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in crypted_text:
    index = key.index(letter)
    plain_text += characters[index]

print (f"orginal message: {crypted_text}")
print (f"encrypted message: {plain_text}")