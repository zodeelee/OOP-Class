class Customer:
    def __init__(self):
        self.cid = input("Enter the customer ID:")
        self.acc_no = input("Enter the account number:")
        self.cname = input("Enter the customer name:")
        self.phone = input("Enter the phone number:")
        self.emailid = input("Enter the email:")
        self.balance = int(input("Enter the account balance:"))

    def debit_from(self, amt):
        self.balance -= amt

    def credit_to(self, amt):
        self.balance += amt

    def display(self):
        print("\n[Customer ID]:", self.cid,
              "\n [Account Number]:", self.acc_no,
              "\n [Customer Name]:", self.cname,
              "\n [Phone Number]:", self.phone,
              "\n [Email ID]:", self.emailid,
              "\n [Total Balance]:", self.balance)

#<><><><><><><><<>><><><><<><><>MAINCODE<><><><><><><><><><<><><><><><><><><><><>

while 1:
    print("<-------------------------------------------------->"
          "\n1. Select Debit Option",
          "\n2. Select Credit Option",
          "\n2. Exit\n"
          "<-------------------------------------------------->\n")
    option = input("[Enter your choice]:")



    c1 = Customer()
    c2 = Customer()

    c1.display()
