def check_number(user_input):
    for character in user_input:
        if character not in "0123456789":
            print("you have not entered a valid number")
            return False
    return True

def get_number():
    while True:
        user_input = input("Enter a number: ")
        if check_number(user_input):
            return int(user_input)
        else:
            print("Please enter a number")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num2 - num1

def multiply(num1, num2):
    return num1 * num2

def divide(a,b):
    return a / b

def square(a):
    return a * 2

def calculator():
    keep_running = True

    options = ["add", "subtract", "multiply", "divide", "square", "quit"]

    while keep_running:
        print("Enter a number: ")
        for i in range(len(options)):
            print(f"{i + 1}: {options[i]}")

        user_input = get_number()
        user_choice = options[user_input - 1]

        if user_choice == "add":
            print("addition")
            num1 = get_number()
            num2 = get_number()
            answer = add(num1, num2)
            print(f"{num1} + {num2} = {answer}")
        elif user_choice == "subtract":
            print("subtraction")
            num1 = get_number()
            num2 = get_number()
            answer = subtract(num1, num2)
            print(f"{num1} - {num2} = {answer}")
        elif user_choice == "multiply":
            print("multiplication")
            num1 = get_number()
            num2 = get_number()
            answer = multiply(num1, num2)
            print(f"{num1} * {num2} = {answer}")
        elif user_choice == "divide":
            print("division")
            num1 = get_number()
            num2 = get_number()
            answer = divide(num1, num2)
            print(f"{num1} / {num2} = {answer}")
        elif user_choice == "square":
            print("squaring")
            num1 = get_number()
            answer = square(num1)
            print(f"{num1} ^ 2 = {answer}")
        elif user_choice == "quit":
            print("quitting")
            keep_running = False
        else:
            print("Please enter a valid input")

calculator()