class BMS:
    def __init__(self):
        self.books = []
        global a

    def add_books(self):
        print("---------------------*******-------------------")
        while True:
            a = input("Add book to the system: ")
            if not a:
                break
            self.books.append(a)
        print("Books added successfully")
        print("---------------------*******-------------------")

    def borrow_books(self):
        print("---------------------*******-------------------")
        a = input("Enter your Book Name: ")
        while a not in self.books:
            print("---- OOPS ! your Books not in our Vault -----")
            print("Please type the book name in the below list")
            self.all_books()
            a = input("Enter your Book Name: ")

        if a in self.books:
            self.books.remove(a)
        print(f"{a} Book can be Borrowed Successfully")
        print("Now available Books in your Vault")
        self.all_books()
        print("---------------------*******-------------------")

    def return_books(self):
        print("---------------------*******-------------------")
        a = input("Enter your Book: ")
        while a in self.books:
            print("---- OOPS ! your Book is already in your vault -----")
            print("---- Please type the Books that not in the below list")
            self.all_books()
            a = input("Enter your Book Name: ")
        if a not in self.books:
            self.books.append(a)
            print(f"{a} Books can be Returned successfully")
            self.all_books()
        print("---------------------*******-------------------")

    def all_books(self):
        print("---------------------*******-------------------")
        print(self.books)
        print("---------------------*******-------------------")

    def logout(self):
        quit()

    def main(self):
        msg = ("---------------------*******------------------- \n"
               "-- Welcome to the GR Books Management System -- \n"
               "1. Add Books \n"
               "2. Books List \n"
               "3. Borrow Books \n"
               "4. Return Books\n"
               "5. Logout \n"
               "---------------------*******-------------------")
        while True:
            print(msg)
            user_choice = int(input("Enter your Option: "))
            while user_choice not in [1, 2, 3, 4, 5]:
                print("---- OOPS ! please select above option correctly ----")
                user_choice = int(input("Enter Your Option: "))
            if user_choice == 1:
                self.add_books()
            elif user_choice == 2:
                self.all_books()
            elif user_choice == 3:
                self.borrow_books()
            elif user_choice == 4:
                self.return_books()
            elif user_choice == 5:
                print("----- Bye Bye ------")
                self.logout()


GR = BMS()
GR.main()

