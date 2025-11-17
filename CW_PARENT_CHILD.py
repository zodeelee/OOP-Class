# Abstraction - information hiding - external users
# Encapsulation - designers
# Inheritance - Reusability
# [CHILD CLASS, PARENT CLASS, WE WILL USE INHERITANCE FOR INTERCHANGEABILITY - POLYMORPHISM]

class Person: # Parent class
    def __init__(self, nn, dd, gg):
        self.pname = nn
        self.dob = dd
        self.gender= gg

    def display(self):
        print("Person Name:", self.pname,
              "\n Person DOB:", self.dob,
              "\n Person Gender:", self.gender)
        return ""

class Student(Person): # Child class
    def __init__(self, x, y, z, a, b):
        Person.__init__(self, x, y, z)
        self.dept = a
        self.id = b

    def display(self):
        print(Person.display(self),
              "\n Student Department:", self.dept,
              "\n Student ID:", self.id)

class Faculty(Person):
    def __init__(self, x, y, z, a, b):
        Person.__init__(self, x, y, z)
        self.email = a
        self.job = b

    def display(self):
        print(Person.display(self),
              "\n Faculty Email:", self.email,
              "\n Faculty Job:", self.job)

# ==== MAIN CODE ====
s1=Student("Jim", "2004", "Male", "CS", "123")
s1.display()

s1=Faculty("Johnathan", "1994", "Male", "johnsolomon@gmail.com", "Math Teacher")
s1.display()