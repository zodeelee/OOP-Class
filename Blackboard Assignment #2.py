#program to calculate the loan repayment

p = int(input(""))
r = int(input(""))
t = int(input(""))

emi = p *r * ((1+r)**n)/((1+r)**n - 1)
for i in range(1,n):
    print(p-emi)