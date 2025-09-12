x = int()
myList = []

while True:
    print("---------------------------------------")
    print("1. Add an Element to the list \n"
          "2. Remove an Element from the list \n"
          "3. Replace an Element from the list \n"
          "4. Sort the Elements in the list \n"
          "5. Reverse the Elements in the list \n"
          "6. Print the list Elements \n"
          "7. Exit \n")
    print("---------------------------------------")

    option = input("Enter your choice:")
    print("---------------------------------------")

    if option == "1":
        myList.append(input("Input to add an Element:"))
        print(myList)
    elif option == "2":
        myList.remove(input("Input to remove an Element:"))
        print(myList)
    elif option == "3":
        print("'Values are sorted from the first number in the list as zero, then one, and so on.'")
        user = int(input("Enter an index value:"))
        myList[user] = input("Input to replace an Element:")
        print(myList)
    elif option == "4":
        myList.sort()
        print(myList)
    elif option == "5":
        myList.reverse()
        print(myList)
    elif option == "6":
        print(myList)
    elif option == "7":
        print("You have quit the program")
        break





