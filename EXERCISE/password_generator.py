import string
import random

characters = list(string.ascii_letters + string.digits + "!@-#$%^_&*()" )


def generate_password():
    password_length = int(input("How long will be the password: "))
    random.shuffle(characters)
    password= []

    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)

    password ="".join(password)
    print(password)

while True:
    option = input("Do you want to create a password?  Use 'yes' or 'no': ")
    if option.lower() == 'yes':
        generate_password()
        quit()
    elif option.lower() == 'no':
        print("Program ended")
        quit()
    elif option.upper() == "Q":
        quit()
    else:
        print("Invalid option, use (Yes/No) or press 'q' to leave the program\n")
        continue