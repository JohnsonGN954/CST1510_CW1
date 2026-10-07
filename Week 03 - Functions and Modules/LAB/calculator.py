"""Define a function add(n1, n2) that returns n1 + n2.
Define a function subtract(n1, n2) that returns n1 - n2.
Define a function multiply(n1, n2) that returns n1 * n2.
Define a function divide(n1, n2) that returns n1 / n2.
Use input() to ask for the first number. Convert it with float() and store it in n1.
Create a variable keep_going and set it to True.
Start a while keep_going: loop.
Inside the loop, ask for an operator (+ - * /) and store it in operator.
Ask for the second number, convert it with float(), and store it in n2.
Use if/elif to call the matching function and store the answer in result. For example, if operator == "+", then result = add(n1, n2).
Print the calculation and the result.
Ask the user: "Type 'y' to continue with the result, or 'n' to start over:"
If they type "y", set n1 = result.
Otherwise, ask for a new first number and store it in n1."""




def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
n1 = float(input("Enter the first number: "))
keep_going = True
while keep_going:
    operator = input("Enter an operator (+, -, *, /): ")
    n2 = float(input("Enter the second number: "))
    if operator == "+":
        result = add(n1, n2)
    elif operator == "-":
        result = subtract(n1, n2)
    elif operator == "*":
        result = multiply(n1, n2)
    elif operator == "/":
        result = divide(n1, n2)
    else:
        print("Invalid operator.")
        continue
    print(f"{n1} {operator} {n2} = {result}")
    choice = input("Type 'y' to continue with the result, or 'n' to start over,or 'q' to quit: ")
    if choice.lower() == "y":
        n1 = result
    elif choice.lower() == "q":
        keep_going = False
    else:
        n1 = float(input("Enter a new first number: "))
