
print()
print("-" * 40)
print("🧮 Welcome to EXPONENTRON 1.0")
print("-" * 40)
print("You enter the numbers for computation — I obey... probably.")
print()

def format_num(n):
    # Converts floats like 2.0 to 2, keeps 2.5 as is
    return f"{int(n)}" if n.is_integer() else f"{n}" 


while True:

    # Input: list of numbers
    user_input = list(map(float, input("Enter numbers separated by spaces: ").split())) 

    # Input: desired power
    power_input = input("Enter the power you want to raise each number to: ").strip()

    if not power_input.lstrip("-").isdigit():
        print("Sorry, I can only handle integer powers for now!")
        continue

    power = int(power_input)


    # Processing each number
    for num in user_input:
        if num == 0 and power < 0:
            print(f"{format_num(num)} --- Whoa! Zero to a negative power? That's black hole stuff. I'm out.")

        elif num == 0:
            print(f"{format_num(num)} --- Easy there, zero raised to any power is still zero...")

        elif num < 0:
            print(f"{format_num(num)} --- Negative? What do you think I am, a complex number calculator?")

        elif num >= 500:
            print(f"{format_num(num)} --- Whoa! Too big. Do the math yourself!")

        else:
            result = num ** power  
            print(f"You entered the number {format_num(num)}| Raised to the power of {power}, it equals {format_num(result)}")

    print("-" * 40)
    print("Calculation complete!") 
    
    # Ask user if they want to run again
    decision = input("Got more numbers to power up? Y/n?").strip().lower()

    if decision == "n":
        print("Bye!")
        break

    elif decision == "y":
        continue

    else:
        print("I'll take that as a yes 😏")
        continue