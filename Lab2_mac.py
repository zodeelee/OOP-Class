myStudents = {}

while True:
    print("1. Add a student \n"
          "2. Remove a student \n"
          "3. Modify a student \n"
          "4. Display all students \n"
          "5. Quit the program \n")
    option = input("Select an option out of the 5 choices:")
    if option == "1":
        print("------------------------------") #linebreaker
        ssid = input("Enter student ID (number):")
        if ssid in myStudents:
            print("That student ID is already in use. Choose another number.")
            continue
        nname = input("Add your name:")
        plab = print("Enter all the points from your lab assignments (out of 10)")
        print("------------------------------") #linebreaker
        Lab1 = int(input("Points from Lab 1:"))
        Lab2 = int(input("Points from Lab 2:"))
        Lab3 = int(input("Points from Lab 3:"))
        Lab4 = int(input("Points from Lab 4:"))
        Lab5 = int(input("Points from Lab 5:"))
        Total = (Lab1+Lab2+Lab3+Lab4+Lab5)
        MaxTotal = 50
        Percent = (Total/MaxTotal) * 100
        Average = Total / 5
        myStudents.update({ssid:{
                "name": nname,
                "Lab01": Lab1,
                "Lab02": Lab2,
                "Lab03": Lab3,
                "Lab04": Lab4,
                "Lab05": Lab5,
                "Total": Total,
                "Percent": Percent,
                "Average": Average,}})
        print("------------------------------") #linebreaker
        for sid in myStudents: #indentation for the dictionary in the output
            print({sid: myStudents[sid]})
            print()
        print("------------------------------")  #linebreaker
    elif option == "2":
        sid = input("Enter the student ID to remove: ")
        if sid in myStudents:
            del myStudents[sid]
            print("Student ID removed.")
        else:
            print("Student ID not found.")
    elif option == "3":
        myStudents = input("Modify a student ID:")
    elif option == "4":
        print("------------------------------") #linebreaker
        sd = print("All the current students in the dictionary")
        print(myStudents)
        print("------------------------------") #linebreaker
    elif option == "5":
        print("You have stopped the program")
        break