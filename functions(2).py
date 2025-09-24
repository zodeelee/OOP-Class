queue = []


def enqueue(): #defined function // add to the que
    queue.append(input("Enter your name to the list:"))

def dequeue(): #defined function // remove from the que
    queue.remove(input("Enter to remove your name from the list:"))

def display(): #defined function // display the que
    print(queue)

while 1:
    print("1. Add yourself to the queue\n"
          "2. Remove yourself from the queue\n"
          "3. Display yourself on the queue\n")

    option = int((input("Choose one of the 3 options:")))
    if option == 1:
        print("------------------------------------")
        print("You've added yourself to the queue!")
        print("------------------------------------")
        enqueue()
    elif option == 2:
        print("------------------------------------")
        print("You've removed yourself from the queue!")
        print("------------------------------------")
        dequeue()
    elif option == 3:
        print("------------------------------------")
        print("You've displayed yourself on the queue!")
        print("------------------------------------")
        display()


