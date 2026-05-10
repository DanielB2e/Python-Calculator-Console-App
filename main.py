def call_header():
    global last_number
    calc_header = f"""
    | PYTHON CALCULATOR |

    Last number received: {last_number}

    1. +
    2. -
    3. *
    4. /
    5. %
    6. **
    q. QUIT
    """
    print(calc_header)

def result_calculation(math_func):
    global last_number
    result = math_func()
    last_number = result
    print(f"\nThe result is: {result}\n")


def call_addition():
    global last_number

    if last_number == None:
        last_number = int(input("No last number! Please enter the First Number: "))
        second_number = int(input("Enter the second number: "))
    else:
        second_number = int(input("Enter the Second Number: "))
    
    return last_number + second_number

def call_substraction():
    global last_number

    if last_number == None:
        last_number = int(input("No last number! Please enter the First Number: "))
        second_number = int(input("Enter the second number: "))
    else:
        second_number = int(input("Enter the Second Number: "))
    
    return last_number - second_number

def call_multiplication():
    global last_number

    if last_number == None:
        last_number = int(input("No last number! Please enter the First Number: "))
        second_number = int(input("Enter the second number: "))
    else:
        second_number = int(input("Enter the Second Number: "))
    
    return last_number * second_number

def call_division():
    global last_number

    if last_number == None:
        last_number = int(input("No last number! Please enter the First Number: "))
        second_number = int(input("Enter the second number: "))
    else:
        second_number = int(input("Enter the Second Number: "))
    
    return last_number / second_number

def call_rest():
    global last_number

    if last_number == None:
        last_number = int(input("No last number! Please enter the First Number: "))
        second_number = int(input("Enter the second number: "))
    else:
        second_number = int(input("Enter the Second Number: "))
    
    return last_number % second_number

def call_power():
    global last_number

    if last_number == None:
        last_number = int(input("No last number! Please enter the First Number: "))
        second_number = int(input("Enter the second number: "))
    else:
        second_number = int(input("Enter the Second Number: "))
    
    return last_number ** second_number

running = True
last_number = None

call_header()

while running:
    choice = input("Select an option: ")

    match choice:
        case "1":
            print("\n| Addition |\n")
            result_calculation(call_addition)
            input("Press ENTER to Continue!")
            call_header() 
        case "2":
            print("\n| Substraction |\n")
            result_calculation(call_substraction)
            input("Pres ENTER to Continue!")
            call_header()
        case "3":
            print("\n| Multiplication |\n")
            result_calculation(call_multiplication)
            input("Pres ENTER to Continue!")
            call_header()
        case "4":
            print("\n| Division |\n")
            result_calculation(call_division)
            input("Pres ENTER to Continue!")
            call_header()
        case "5":
            print("\n| Rest |\n")
            result_calculation(call_rest)
            input("Pres ENTER to Continue!")
            call_header()
        case "6":
            print("\n| Power |\n")
            result_calculation(call_power)
            input("Pres ENTER to Continue!")
            call_header()
        case "q":
            print("\nThank you for using my Calculator App!\n")
            running = False
        case _:
            print("\nPlease enter a valid option!\n")