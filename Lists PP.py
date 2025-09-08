myList = []


while True:
    print("1. Append to the list\n"
          "2. Remove from the list\n"
          "3. Pop an element from the list\n"
          "4. Display the List\n"
          "5. Quit\n")


    option = input("Enter your choice:")

    if option == "1":
        n = input("Enter a value to add to the list")
        myList.append(n)
        print(myList)
