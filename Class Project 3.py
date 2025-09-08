#Find the greatest number of the three
a_user= int(input("User A, Put a number: "))
b_user= int(input("User B, Put a number: "))
c_user= int(input("User C, Put a number: "))

if a_user > b_user and a_user > c_user:
    print("User A is greater")

elif b_user > c_user and b_user > a_user:
    print("User B is greater")

else:
    print("User C is greater than user B and user A")


