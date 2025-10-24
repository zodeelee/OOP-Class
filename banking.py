class Customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.cname = ""
        self.phone = ""
        self.emailid = ""
        self.balance = 0

    def debit_from(self, amt):
        self.balance -= float(input("Enter the amount to send:"))

    def credit_to(self, amt):
        self.balance += float(input("Enter the amount to receive:"))

    def add_customer(self):
        self.cid = input("Enter customer ID:")
        self.acc_no = input("Enter account number:")
        self.cname = input("Enter customer name:")
        self.phone = input("Enter phone number:")
        self.emailid = input("Enter email ID:")
        self.balance = int(input("Enter balance:"))

    def display_info(self):
        print("\n[Customer ID]:", self.cid,
              "\n [Account Number]:", self.acc_no,
              "\n [Customer Name]:", self.cname,
              "\n [Phone Number]:", self.phone,
              "\n [Email ID]:", self.emailid,
              "\n [Total Balance]:", self.balance)

#<><><><><><><><<>><><><><<><><>MAINCODE<><><><><><><><><><<><><><><><><><><><><>


c1 = Customer()
c2 = Customer()

c1.add_customer()
c2.add_customer()

c1.debit_from(amt=100)
c2.credit_to(amt=-100)

c1.display_info()
c2.display_info()

