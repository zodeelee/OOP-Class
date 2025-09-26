myList = [] #global variable
a=10

def function1(r):
    r=r+1
    area = 2*3.14*r
    return area

def functon2():
    a=50
    b="Justus" #local variable for this function()

#main code

while True:
    name = "Justus"
    radius = 10
    calculated_area = function1(radius)
    print(calculated_area)

