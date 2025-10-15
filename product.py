import pickle
class Product:
    def __init__(self):
        self.pid = ""
        self.pname = ""
        self.price = 0.0
        self.description = ""

    def get_product_details(self):
        self.pid = input("Please enter an ID:")
        self.pname = input("Please enter a name:")
        self.price = int(input("Please enter a price:"))
        self.description = input("Please enter a description:")

    def display_product_info(self):
        print("\n[product ID]:", self.pid,
              "\n[product name]:", self.pname,
              "\n[product price]:", self.price,
              "\n[product description]:", self.description)


#<><><><><><><<<><><><><<>MAIN_CODE<><><><><>><><><><><<><><><><><<><><>

while 1:
    print("<----------------------------------------------------------->\n"
          "1. show a menu to create a  product object\n",
          "2. get info for the product\n",
          "3. display the product\n",
          "4. write the product into a file\n",
          "5. read from the file\n",
          "6. Exit\n"
          "<----------------------------------------------------------->\n")

    option = input("Enter your option:")
    product_obj = Product() #option == 1

    product_obj.get_product_details() #option == 2

    product_obj.display_product_info() #option == 3

    if option == 4:
        f1 = open("product_inventory.dat", "ab")
        pickle.dump(product_obj, f1)
        f1.close()

#<><><><><>><><><><><<><><><><><<><><><><><><><>><><><><><<><><><><><<><>