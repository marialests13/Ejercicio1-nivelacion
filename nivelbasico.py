
# 1. Guarde la contraseña correcta en una variable

pass_word = "admin123"

# 2. Pida al usuario ingresar una contraseña.
print("Please put a password using 5 letters and 3 numbers")

user_password = input()
if user_password == pass_word:
    print("Congratulations, this is the correct password")
elif user_password != pass_word:
    print("Incorrect, try again")