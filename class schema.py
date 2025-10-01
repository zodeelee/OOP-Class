class Student:
    def __init__(self): #constructor function
        self.stu_id = ""
        self.stu_Name = ""
        self.major = ""
        self.gpa = 0.0
        self.dob = ""
    def add_student(self):
        self.StuID = int(input("Enter Student ID:"))
            try:
                print("")
        self.name = input("Enter Student Name:")
        self.major = input("Enter Student Major:")
        self.gpa = input("Enter student GPA:")
        self.dob = input("Enter Date of Birth:")

    def edit_student(self):
        self.StuID = int(input("Enter the updated ID for Student:"))
        self.stu_Name = input("Enter the updated Name for the Student:")
        self.major = input('Enter the updated Major for the Student:')
        self.gpa = int(input('Enter the updated GPA for the Student:'))
        self.dob = input("Enter the updated DOB for the Student:")

    def display_student(self):
        print("Student ID:", self.StuID,
              "\n Student Name:", self.stu_Name,
              "\n Student Major:", self.major,
              "\n Student GPA:", self.gpa,
              "\n Student DOB:", self.dob)

#Main Code
s1 = Student()  #create an object, it calls the CONSTRUCTOR function

s1.add_student()
s1.display_student()

s2 = Student()
s3 = Student()
s3.display_student()

