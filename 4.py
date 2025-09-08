#operator +, -, *, / get this from the user
#think of it like a calculator, u can ask for an input +, -, * (multiplication), / (division), and return both values
#for the user depending on the input you give it.


num_1 = int(input("Input value: "))
num_2 = int(input("Input value: "))
operator = input("Enter what operation you want to perform:")


if operator == "+":
    print("The sum is:", num_1+num_2)
elif operator == "-":
    print("The sum is:", num_1-num_2)
elif operator == "*":
    print("The sum is:", num_1*num_2)
elif operator == "/":
    print("The sum is:", num_1/num_2)


