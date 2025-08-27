print("Hello student, please enter your name and coursework grades.")

stu_name = input("Enter your name: ")
course1= int(input("Enter the grade points for Course1: "))
course2= int(input("Enter the grade points for Course1: "))
course3= int(input("Enter the grade points for Course1: "))
course4= int(input("Enter the grade points for Course1: "))
course5= int(input("Enter the grade points for Course1: "))

#Typecasting: changing the data type from one form to the other from strings to integers

total = course1+course2+course3+course4+course5
average = course1+course2+course3+course4+course5 / 5

#Total/Average: Get the total grade from all the students coursework, then get their average score

print("Student:", stu_name, ". Your total coursework grade:", total, ". Your total average grade:", average)


