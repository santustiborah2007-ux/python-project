import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789#*$@%"
password = ""
for i in range(8):
    password += random.choice(characters)
print("Generated Password:", password)