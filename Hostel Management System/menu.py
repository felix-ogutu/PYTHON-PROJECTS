def menu():
    print("[1] Option 1")
    print("[2] Option 2")
    print("[0]  Exit the program")

    menu()
    option = int(input("Enter the option:"))

    while option != 0:
        if option == 1:
            print("Option 1 has been selected")
        elif option == 2:
            print("Option 2 has been  selected")
        else:
            print("Invalid choice has been selected")

            print()
            menu()
            option = int(input("Enter your option:"))
            print("Thank you for using this program. Goodbye")
