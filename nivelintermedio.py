# 1. Desarrolla un programa que verifique si una contraseña cumple con los requisitos mínimos de seguridad. 
#La contraseña debe tener al menos 8 caracteres y contener al menos un número.
print("Please, put a password")

while True: 
    pass_word = input()
    if len(pass_word) == 8 and any(char.isdigit() for char in pass_word):
        print("You're doing amazing. This password is perfetc")
        break
    else:
        print("This password is not good, please put another using 8 characters and a number")
