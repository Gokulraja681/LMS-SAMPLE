import random


class GRB:
    def __init__(self):
        self.name = ""
        self.fname = ""
        self.age = 0
        self.mob = 0
        self.pl = ""
        self.tl = ""
        self.ACN = 0
        self.acm = 0
        self.mpin = 0

    def welcome_message(self):
        print("\n-------------*********--------------")
        print("--- Welcome to the GRB Bank ---")
        print("1. Account Holder profile")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Balance Enquiry")
        print("5. Edit M-Pin")
        print("6. Logout")
        print("-------------*********--------------\n")

    def account_creation(self):
        print("------ Welcome to GRB Bank ! ------")
        print("------ Account Creation ! --------\n")
        print("-------------*********--------------")
        self.name = input("Enter Your Name: ")
        self.fname = input("Enter Your Father's Name: ")
        self.age = int(input("Enter Your Age: "))
        self.mob = int(input("Enter Your Mobile Number: "))
        self.pl = input("Enter Your Permanent Location: ")
        self.tl = input("Enter Your Temporary Location: ")
        print("-------------------------------------------------")
        print("To confirm Account Creation deposit amount 500")
        self.acm = int(input("Account initial Amount: "))
        print("-------------------------------------------------")
        while self.acm < 500:
            print("Minimum Deposit Amount is 500")
            self.acm = int(input("Account initial Amount: "))
        print("---- Initial Deposit Amount has added Successfully ! ----")
        print("-------------------------------------------------")
        self.create_mpin()
        print("----- Account has been created successfully! -----")
        print("-------------*********--------------\n")

    def account_profile(self):
        print("\n-------------*********--------------")
        print("--- Account Holder Profile ----")
        acn = random.randint(1, 15)
        self.ACN = acn
        print(f"Account Number: 2480100017432{self.ACN}")
        print("Your Account Pin: ", self.mpin)
        print("Account Balance: ", self.acm)
        print("Your Name: ", self.name)
        print("Your Father's Name:", self.fname)
        print("Your Age:", self.age)
        print("Your Mobile Number:", self.mob)
        print("Your Permanent Location:", self.pl)
        print("Your Temporary Location:", self.tl)
        print("-------------*********--------------\n")

    def create_mpin(self):
        print("------ Create Passcode for your Account ------")
        self.mpin = input("Create M-Pin: ")
        while len(self.mpin) != 4:
            print("---- OOPS !  M-Pin can be four characters only ----")
            self.mpin = input("Create M-pin: ")
        c_mpin = input("Confirm M-Pin: ")
        while c_mpin != self.mpin:
            print("---- OOPS ! Cannot Match with M-Pin ----")
            c_mpin = input("Confirm M-Pin: ")
        if self.mpin == c_mpin:
            print("---- M-Pin has been Generated Successfully ! ----")
            print("Your M-Pin is: ", self.mpin)
        else:
            print("failure")
        print("-------------------------------------------------")

    def edit_mpin(self):
        q = input("Enter you M-pin: ")
        while q != self.mpin:
            print("---- OOPS! M-Pin not Matched ----")
            q = input("Enter you M-pin: ")
        self.mpin = input("Create M-Pin: ")
        while len(self.mpin) != 4:
            print("---- OOPS !  M-Pin can be four characters only ----")
            self.mpin = input("Create M-pin: ")
        c_empin = input("Confirm M-Pin: ")
        while c_empin != self.mpin:
            print("---- OOPS ! Cannot Match with M-Pin ----")
            c_empin = input("Confirm M-Pin: ")
        if self.mpin == c_empin:
            C_Pin = self.mpin
            print("---- M-Pin has been Edited Successfully ! ----")
            print("Your M-Pin is: ", self.mpin)


    def balance_enquiry(self):
        print("\n---- Balance Enquiry ----")
        global q
        q = input("Enter your M-Pin: ")
        while q != self.mpin:
            print("---- OOPS! M-Pin not Matched ----")
            q = input("Enter your M-Pin: ")
        print("Account Holder: ", self.name)
        print(f"Account Number: 2480100017432{self.ACN}")
        print("Current Account Balance: ", self.acm, "\n")

    def deposit_amount(self):
        print("-------------*********--------------")
        print("Minimum Deposit Amount: 500")
        deposit_amount = int(input("Enter Deposit Amount: "))
        while deposit_amount < 500:
            print("Minimum Deposit Amount is 500")
            deposit_amount = int(input("Enter Deposit Amount: "))
        self.acm += deposit_amount
        print("----To confirm Deposit Amount please enter your M-Pin below ----")
        q = input("Enter your M-Pin: ")
        while q != self.mpin:
            print("---- OOPS! M-Pin not Matched ----")
            q = input("Enter your M-Pin: ")
        print(f"{deposit_amount} has been credited to your Account")
        print("Current Balance: ", self.acm)
        print("--- Amount Deposited Successfully ---")
        print("-------------*********--------------\n")

    def withdraw_amount(self):
        print("-------------*********--------------")
        print("Minimum Withdraw Amount: 500")
        withdraw_amount = int(input("Enter Withdraw amount: "))
        while withdraw_amount < 500 or withdraw_amount > self.acm:
            if withdraw_amount < 500:
                print("Minimum Withdraw Amount is 500")
            else:
                print("Insufficient funds. Enter a valid amount.")
            withdraw_amount = int(input("Enter Withdraw amount: "))
        self.acm -= withdraw_amount
        print("----To confirm Withdraw Amount please enter your M-Pin below ----")
        q = input("Enter your M-Pin: ")
        while q != self.mpin:
            print("---- OOPS! M-Pin not Matched ----")
            q = input("Enter your M-Pin: ")
        print(f"{withdraw_amount} has been debited from your Account")
        print("Current Balance: ", self.acm)
        print("---- Amount Withdrawal Successful ----")
        print("-------------*********--------------\n")

    def main(self):
        print("---- Please Create an Account First ! ----")
        self.account_creation()
        while True:
            self.welcome_message()
            user_choice = int(input("Enter Your Request: "))
            while user_choice not in [1, 2, 3, 4, 5, 6]:
                print("----- OOPS! Enter a valid Request -----")
                user_choice = int(input("Enter Your Request: "))
            if user_choice == 1:
                self.account_profile()
            elif user_choice == 2:
                self.deposit_amount()
            elif user_choice == 3:
                self.withdraw_amount()
            elif user_choice == 4:
                self.balance_enquiry()
            elif user_choice == 5:
                self.edit_mpin()
            elif user_choice == 6:
                print("---- Thank You for Visiting Our GRB BANK ! ----")
                break


grb_bank = GRB()
grb_bank.main()
