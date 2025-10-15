#file1 = open("test1.txt", "w")

#file1.writelines("Hello World!\n")
#file1.writelines("Welcome to OOP course\n")
#file1.writelines("Have a good \n")

#.close()

#file2 = open("test1.txt", "r")

#for line in file2:
    #print(line)

#file2.close()

import pickle

d = {
    "stu1": {"Name": "John", "Age": "21", "Id": 28},
    "stu2": {"Name": "Bob", "Age": "99", "Id": 28},
    "stu3": {"Name": "Jason", "Age": "70", "Id": 28},
    "stu4": {"Name": "Alex", "Age": "55", "Id": 28},
      }

with open("myUsers.dat", "wb") as file1:
    pickle.dump(d,file1)
file1.close()

with open("myUsers.dat", "rb") as file2:
    myDictionary = pickle.load(file2)

print(myDictionary["stu1"]["Name"])

i = 1
for x in myDictionary:
    var = "stu"+str(i)
    print(myDictionary[var]["Name"])
    i +=1