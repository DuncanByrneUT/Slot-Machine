#GLOBAL CONSTANT
MAX_LINES = 5

# deposit amount function
def deposit():
    while True:
        amount = input("Please enter the amount you'd like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

# number of lines
def get_number_of_lines():
    while True:
        lines = input("Please enter the number of lines you'd like to bet on. (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines



# main function
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)
main()