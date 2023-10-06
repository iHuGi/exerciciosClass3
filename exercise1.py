
# First Try, function to check if odd or even
print("VERSION 1")
def check_even_odd():
    while True:
        try:
            user_input = int(input("Enter a number: "))
            if user_input % 2 == 0:
                print(f"{user_input} is even.")
            else:
                remainder = user_input % 2
                print(f"{user_input} is odd with a remainder of {remainder}.")
            break # Exit the loop if the input from the user is valid
        except ValueError as e:
            print(f"Error: Invalid number!")

# To use the function:
check_even_odd()


print("")


# Second Try, function to check if odd or even
print("VERSION 2")
def check_is_odd_or_even():
    while True:
        try:
            str_number = input("Enter a number: ")
            number = int(str_number)
            if number % 2 == 0:
                print(f"{number} is even.")
            else:
                remainder = number % 2
                print(f"{number} is odd with a remainder of {remainder}.")
            break  # Exit the loop if the input from the user is valid
        except ValueError as e:
            print(f"Error: Invalid number!")

# To use the function:
check_is_odd_or_even()


print("")


# Third and final try
print("VERSION 3")
def check_is_odd_or_even():
    while True:
        try:
            str_number = input("Enter a number: ").rstrip().lstrip()
            if not str_number.isdigit():
                raise ValueError("Invalid Number!")
            else:
                number = int(str_number)
                if number % 2 == 0:
                    print(f"{number} is even.")
                else:
                    remainder = number % 2
                    print(f"{number} is odd with a remainder of {remainder}.")
                break  # Exit the loop if the input from the user is valid
        except ValueError as e:
            print(f"Error: {e}")

# To use the function:
check_is_odd_or_even()


