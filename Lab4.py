class Customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.cname = ""
        self.phone = ""
        self.emailid = ""
        self.balance = 0
        self.card = []

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

class Card:
    def __init__(self):
        self.type = ""
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = 0

    def card_info(self):
        self.type = input("Enter card type:")
        self.card_no = input("Enter card number:")
        self.cvv = input("Enter card CVV:")
        self.expiry_date = input("Enter expiry date:")
        self.balance = int(input("Enter your balance:"))

    def display(self):
        print("\n[Card_Type]:", self.type,
              "\n [Card_Number]:", self.card_no,
              "\n [CVV]:", self.cvv,
              "\n [Expiry Date]:", self.expiry_date,
              "\n [Balance]:", self.balance)


#<><><><><><><><<>><><><><<><><><><><><><><><><><><<><><><><><><><><><><>

while 1:
    print("------------------------------------\n"
          "1. Create customer objects\n"
          "2. Crete card objects\n"
          "3. Transfer funds between customer objects\n"
          "4. Assign card objects to customer objects\n"
          "5. Display Customer Info\n"
          "6. Display Card Info\n"
          "7. Commit\n"
          "8. Exit\n"
          "------------------------------------")
    option = int(input("[Select An Option]:"))

    if option == 1:
        customer1 = Customer()
        customer2 = Customer()

    elif option == 2:
        credit_card = Card()
        debit_card = Card()

    elif option == 3:
        try:
            c1.debit_from()
            c2.debit_to()
        except:
            print("An error occured. Please try again.")

    elif option == 4:
        id = int(input("Enter your card ID:"))
        card_type = input("Enter card info:")

    #elif option == 5:

    #elif option == 6:

    #elif option == 7:

    elif option == 8:
        print("You have stopped the program.")
        break




    c1 = Customer()
    c2 = Customer()

    c1.add_customer()
    c2.add_customer()

    c1.debit_from()
    c2.credit_to()

    c1.display_info()
    c2.display_info()
