#collections - Array, Lists, Tuples, Sets, Dictionary
#myList = [2,3,67,9,2,5,6,"Js","Apple"]
#print(myList)

#myList = ["Red", "Green", "Blue"] #Red --> 0, #Green --> 1, #Blue --> 2, and so on. Always starts at zero

#myList[0] = "Purple"
#myList[1] = "Orange"
#myList[2] = "Pink"
for i in range(0, len(myList)):
    print(myList[i])

#print(myList[2])

myList.append(10)

x = input("Enter your name:")
myList.append(x)
print(myList)

myList.pop() #remove the last added element
myList.remove(10)
print(myList)

print(myList)