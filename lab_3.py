from os import WCONTINUED


class Book: #book_id,author_id,publisher,publication date
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.book_author_id = ""
        self.book_publisher = ""
        self.book_pd = 0
        self.bb = []

    def add_book(self): #we need the user to be able to add the book's information
        print()
        self.book_id = int(input("Enter the book ID:"))
        self.book_title = input("Enter the book title:")
        self.book_author_id = input("Enter the ID of the author's book:")
        self.book_publisher = input("Enter the book publisher:")
        self.book_pd = int(input("Enter the publication year of the book:"))
        print()

    def display_book(self): #we also need to display the information of the book's contents
        print("-------------------------------------------------------"
            "\n[ID of Book]:", self.book_id,
            "\n[Title of book]:", self.book_title,
            "\n[Book Author]:", self.book_author_id,
            "\n[Publisher of the book]:", self.book_publisher,
            "\n[Date of publication]:", self.book_pd,
            "\n-------------------------------------------------------")
        print()

class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.author_affiliation = ""
        self.author_email = ""
        self.author_phone = ""
        self.author_country = ""

    def add_author(self):
        self.author_id = int(input("Enter the author ID:"))
        self.author_name = input("Enter the author name:")
        self.author_affiliation = input("Enter the author affiliation:")
        self.author_email = input("Enter the author's email:")
        self.author_phone = input("Enter the author's phone number:")
        self.author_country = input("Enter the country of the author:")
        print()

    def display_author(self):
        print("-------------------------------------------------------"
            "\n[ID of author]:", self.author_id,
            "\n[Author Name]:", self.author_name,
            "\n[Author Affiliation]:", self.author_affiliation,
            "\n[Author Email]:", self.author_email,
            "\n[Author Phone]:", self.author_phone,
            "\n[Author Country]:", self.author_country,
            "\n-------------------------------------------------------")
        print()


class User:
    def __init__(self):
        self.user_id = ""
        self.user_email = ""
        self.user_name = ""
        self.user_password = ""
        self.user_address = ""
        self.bb = []

    def add_user(self):
        self.user_id = int(input("Enter the user's ID:"))
        self.user_email = input("Enter the user's email:")
        self.user_name = input("Enter the user's name:")
        self.user_password = input("Enter the user's password:")
        self.user_address = input("Enter the user's address:")
        print()

    def display_user(self):
        print("-------------------------------------------------------"
            "\n[User ID]:", self.user_id,
            "\n[Email]:", self.user_email,
            "\n[Name]:", self.user_name,
            "\n[Password]:", self.user_password,
            "\n[Address]:", self.user_address,
            "\n[Books Borrowed]:", [book.book_title for book in self.bb],
            "\n-------------------------------------------------------")
        print()


    def borrow_book(self, book):
        self.bb.append(book)
        print(self.user_name + " has borrowed book(s): " + book.book_title)



#<><><><><><><><><><><><><><><MAIN CODE<><><><><><><><><><><><><><><><><><<><><><><><><>
s1 = User()
s2 = Book()

s2.add_book()
s2.display_book()

s1.add_user()
s1.display_user()

s1.borrow_book(s2)

s1.display_user()



