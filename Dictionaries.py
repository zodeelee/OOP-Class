# Test project #1

#myStudents = {"s1":"Justus", "s2":"Jemi"}
#print(myStudents)

#myStudents.update({"s3":"Melba"})
#myStudents.update({"s4":"Melba"})

#print(myStudents)

#del myStudents ["s2"]
#print(myStudents)

#del myStudents ["s3"]
#print(myStudents)

# Test project #2

#myStudents = {}


#myStudents.update({"s2":{
    #"name":"Jakob",
    #"major":"Engineering",
    #"Year":"Sophomore",
    #"credits":35,
    #"gpa":3
#}})

# Test project #3

myStudents = {}

while True:
    print("1. Add a student \n"
          "2. Delete a student \n"
          "3. Edit a student \n"
          "4. Print a student \n"
          "5. Quit \n")
    option = input("Enter your choice from the list: ")
    if option == "1":
        sid = input("Enter Your Student Id:")
        nname = input("Name:")
        mmajor = input("Major:")
        yyear = input("Year:")
        tcredits = int(input("TC:"))
        ggpa = input("GPA:")
        myStudents.update({"s2":{"name"}})
        print(myStudents)

    elif option == "2":
        sid = input("Enter To Delete ID:")
        print(myStudents)
    elif option == "3":
        sid = input("Enter the sid that needs to be edited")
        #myStudent.update(sid:{})
        print(myStudents)
    elif option == "4":
        print(myStudents)
    elif option == "5":
        print("You have quit the program.")
        break





# sid = student id, tc = total credits,




