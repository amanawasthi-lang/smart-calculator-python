import math
from colorama import Fore

history = []


# ==========================
# Helper Functions
# ==========================

def format_number(num):
    """Remove .0 from whole numbers."""
    if isinstance(num, float) and num.is_integer():
        return int(num)
    return num


def save_to_file(calculation):
    with open("history.txt", "a") as file:
        file.write(calculation + "\n")


def save_calculation(calculation):
    history.append(calculation)
    save_to_file(calculation)


def show_result(calculation):
    print(Fore.CYAN + "\n╔══════════════════════════════════════════════╗")
    print(Fore.CYAN + "║" + Fore.GREEN + "                 ✅ RESULT                   " + Fore.CYAN + "║")
    print(Fore.CYAN + "╠══════════════════════════════════════════════╣")
    print(Fore.WHITE + f"║ {calculation:<44}║")
    print(Fore.CYAN + "╚══════════════════════════════════════════════╝")


def get_numbers():
    try:
        num1 = float(input(Fore.YELLOW + "Enter first number : "))
        num2 = float(input(Fore.YELLOW + "Enter second number: "))
        return num1, num2

    except ValueError:
        print(Fore.RED + "\n❌ Invalid input! Please enter valid numbers.")
        return None, None


# ==========================
# Calculator Functions
# ==========================

def addition():
    print(Fore.BLUE + "\n========== ADDITION ==========")

    num1, num2 = get_numbers()

    if num1 is None:
        return

    result = num1 + num2

    calculation = (
        f"{format_number(num1)} + "
        f"{format_number(num2)} = "
        f"{format_number(result)}"
    )

    save_calculation(calculation)
    show_result(calculation)


def subtraction():
    print(Fore.BLUE + "\n========== SUBTRACTION ==========")

    num1, num2 = get_numbers()

    if num1 is None:
        return

    result = num1 - num2

    calculation = (
        f"{format_number(num1)} - "
        f"{format_number(num2)} = "
        f"{format_number(result)}"
    )

    save_calculation(calculation)
    show_result(calculation)


def multiplication():
    print(Fore.BLUE + "\n========== MULTIPLICATION ==========")

    num1, num2 = get_numbers()

    if num1 is None:
        return

    result = num1 * num2

    calculation = (
        f"{format_number(num1)} × "
        f"{format_number(num2)} = "
        f"{format_number(result)}"
    )

    save_calculation(calculation)
    show_result(calculation)


def division():
    print(Fore.BLUE + "\n========== DIVISION ==========")

    num1, num2 = get_numbers()

    if num1 is None:
        return

    try:
        result = num1 / num2

        calculation = (
            f"{format_number(num1)} ÷ "
            f"{format_number(num2)} = "
            f"{format_number(result)}"
        )

        save_calculation(calculation)
        show_result(calculation)

    except ZeroDivisionError:
        print(Fore.RED + "\n❌ Division by zero is not allowed.")

def power():
    print(Fore.BLUE + "\n========== POWER ==========")

    num1, num2 = get_numbers()

    if num1 is None:
        return

    result = num1 ** num2

    calculation = (
        f"{format_number(num1)} ^ "
        f"{format_number(num2)} = "
        f"{format_number(result)}"
    )

    save_calculation(calculation)
    show_result(calculation)


def square_root():
    print(Fore.BLUE + "\n========== SQUARE ROOT ==========")

    try:
        num = float(input(Fore.YELLOW + "Enter a number: "))

        if num < 0:
            print(Fore.RED + "\n❌ Square root of a negative number is not possible.")
            return

        result = math.sqrt(num)

        calculation = (
            f"√{format_number(num)} = "
            f"{format_number(result)}"
        )

        save_calculation(calculation)
        show_result(calculation)

    except ValueError:
        print(Fore.RED + "\n❌ Invalid input! Please enter a valid number.")


def percentage():
    print(Fore.BLUE + "\n========== PERCENTAGE ==========")

    try:
        percent = float(input(Fore.YELLOW + "Enter percentage: "))
        number = float(input(Fore.YELLOW + "Enter number: "))

        result = (percent / 100) * number

        calculation = (
            f"{format_number(percent)}% of "
            f"{format_number(number)} = "
            f"{format_number(result)}"
        )

        save_calculation(calculation)
        show_result(calculation)

    except ValueError:
        print(Fore.RED + "\n❌ Invalid input! Please enter valid numbers.")


def modulus():
    print(Fore.BLUE + "\n========== MODULUS ==========")

    num1, num2 = get_numbers()

    if num1 is None:
        return

    try:
        result = num1 % num2

        calculation = (
            f"{format_number(num1)} % "
            f"{format_number(num2)} = "
            f"{format_number(result)}"
        )

        save_calculation(calculation)
        show_result(calculation)

    except ZeroDivisionError:
        print(Fore.RED + "\n❌ Cannot perform modulus by zero.")


def show_history():
    print(Fore.CYAN + "\n╔══════════════════════════════════════════════╗")
    print(Fore.CYAN + "║" + Fore.GREEN + "          📜 CALCULATION HISTORY            " + Fore.CYAN + "║")
    print(Fore.CYAN + "╚══════════════════════════════════════════════╝")

    try:
        with open("history.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print(Fore.YELLOW + "\nNo calculations found.")
            return

        for i, line in enumerate(lines, start=1):
            print(Fore.WHITE + f"{i}. {line.strip()}")

    except FileNotFoundError:
        print(Fore.RED + "\nNo history file found.")


def clear_history():
    history.clear()

    with open("history.txt", "w") as file:
        pass

    print(Fore.GREEN + "\n✅ History cleared successfully.")