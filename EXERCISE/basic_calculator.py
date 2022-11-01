def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer} \n")

def sub(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer} \n")

def mult(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer} \n")

def div(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer} \n")


print("A for addition")
print("B for substraction")
print("C for multiplication")
print("D for division")
print("E for exit")

choice = input("Make your choice: ").upper()

while True:
    if choice == "A":
        print("Addition")
        a = input("type your 1st number: ")
        if a.isdigit():
            a = int(a)
        else:
            print("USE DIGIT ONLY \n")
            continue

        b = input("type your 2nd number: ")
        if b.isdigit():
            b = int(b)
        else:
            print("USE DIGIT ONLY  NEXT TIME \n")
            break
        add(a, b)

    elif choice == "B":
        print("Subtraction")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        sub(a, b)
    elif choice == "C":
        print("Multiplication")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        mult(a, b)
    elif choice == "D":
        print("Division" )
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        div(a, b)
    elif choice == "E":
        print("program ended")
        quit()




