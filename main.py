from colorama import Fore, Style, init
from modules.calculator import (
    addition,
    subtraction,
    multiplication,
    division,
    power,
    square_root,
    percentage,
    modulus,
    show_history,
    clear_history,
)

# Initialize colorama
init(autoreset=True)

while True:
    # Clear screen (optional)
    print("\n" * 2)

    # ==========================
    # Header
    # ==========================
    print(Fore.CYAN + "╔════════════════════════════════════════════════════╗")
    print(Fore.CYAN + "║" + Fore.GREEN + "               🧮 SMART CALCULATOR                 " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.YELLOW + "                    Version 2.0                   " + Fore.CYAN + "║")
    print(Fore.CYAN + "╠════════════════════════════════════════════════════╣")
    print(Fore.CYAN + "║" + Fore.WHITE + "              Built with Python ❤️                " + Fore.CYAN + "║")
    print(Fore.CYAN + "╚════════════════════════════════════════════════════╝")

    print(Fore.WHITE + "\n📋 Select an Operation\n")

    print(Fore.GREEN + " 1." + Fore.WHITE + " Addition")
    print(Fore.GREEN + " 2." + Fore.WHITE + " Subtraction")
    print(Fore.GREEN + " 3." + Fore.WHITE + " Multiplication")
    print(Fore.GREEN + " 4." + Fore.WHITE + " Division")
    print(Fore.GREEN + " 5." + Fore.WHITE + " Power")
    print(Fore.GREEN + " 6." + Fore.WHITE + " Square Root")
    print(Fore.GREEN + " 7." + Fore.WHITE + " Percentage")
    print(Fore.GREEN + " 8." + Fore.WHITE + " Modulus")

    print(Fore.BLUE + " 9." + Fore.WHITE + " Show History")
    print(Fore.RED + "10." + Fore.WHITE + " Clear History")
    print(Fore.MAGENTA + "11." + Fore.WHITE + " Exit")

    print(Fore.CYAN + "\n════════════════════════════════════════════════════")

    choice = input(Fore.YELLOW + "👉 Enter your choice (1-11): ")

    print()

    if choice == "1":
        addition()

    elif choice == "2":
        subtraction()

    elif choice == "3":
        multiplication()

    elif choice == "4":
        division()

    elif choice == "5":
        power()

    elif choice == "6":
        square_root()

    elif choice == "7":
        percentage()

    elif choice == "8":
        modulus()

    elif choice == "9":
        show_history()

    elif choice == "10":
        clear_history()

    elif choice == "11":
        print(Fore.CYAN + "\n════════════════════════════════════════════════════")
        print(Fore.GREEN + "🙏 Thank you for using Smart Calculator!")
        print(Fore.YELLOW + "👋 Goodbye! Have a wonderful day.")
        print(Fore.CYAN + "════════════════════════════════════════════════════")
        break

    else:
        print(Fore.RED + "❌ Invalid choice! Please enter a number between 1 and 11.")

    input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue...")