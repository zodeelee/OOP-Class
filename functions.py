#print()
#input() #function

#append()

#myList.append("blue") #function or method
#myDict.update("value")


def area_of_rectangle(): #definition of function
    l = int(input("Enter length:"))
    b = int(input("Enter breadth:"))
    print(l*b)

def vol_of_cube(): #definition of function volume of cube
    l = int(input("Enter side lengths:"))
    b = int(input("Enter side lengths:"))
    h = int(input("Enter side lengths:"))
    print(l*b*h)

def area_of_circle(): #definition of function volume of cube
    r = int(input("Enter radius:"))
    r = int(input("Enter radius:"))
    print(3.14*r*r)

def volume_of_circle(): #definition of function volume of cube
    r = int(input("Enter radius:"))
    print(2*3.14*r)

def volume_of_sphere(): #definition of function volume of cube
    r = int(input("Enter Enter radius:"))
    r = int(input("Enter Enter radius:"))
    r = int(input("Enter radius:"))
    print(4/3&3.14*r*r*r)


#main code-----------------------

while 1:
    print(
    "1. Area of a rectangle\n" #l*b
    "2. Volume of a cube\n" #l*b*h
    "3. Area of a circle\n" #.14*r*r
    "4. Volume of a sphere\n") #2*3.14*r
    option = int(input("Select one of the four options:"))
    if option == 1:
        print("You've selected area of rectangle")
        area_of_rectangle() #calling of the function
    elif option == 2:
        print("You've selected volume of a cube")
        vol_of_cube()
    elif option == 3:
        print("You've selected area of a circle")
        area_of_circle()
    elif option == 4:
        print("You've selected volume of a sphere")
        volume_of_circle()
    elif option ==5:
        volume_of_sphere()
