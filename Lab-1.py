while True:
    print("Select one of the 5 options in the calculator to perform an action.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    option = input("Please, select an option.")

    if option =="1":
        print("You have chosen addition")
        n1 = int(input("Please enter your first number:"))
        n2 = int(input("Please enter your second number:"))
        print("Your answer:", n1+n2)

    elif option =="2":
        print("You have chosen subtraction")
        n1 = int(input("Please enter your first number:"))
        n2 = int(input("Please enter your second number:"))
        print("Your answer:", n1 - n2)

    elif option =="3":
        print("You have chosen multiplication")
        n1 = int(input("Please enter your first number:"))
        n2 = int(input("Please enter your second number:"))
        print("Your answer:", n1 * n2)

    elif option =="4":
        print("You have chosen division")
        n1 = int(input("Please enter your first number:"))
        n2 = int(input("Please enter your second number:"))
        print("Your answer:", n1 / n2)

    elif option =="5":
        print("You have stopped the program, have a good day.")
        break