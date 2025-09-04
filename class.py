class Person:
    def __init__(self,name):
        self.name = name

    def talks(self):
        print(f"{self.name} is talking")

# person1 = Person("Alvin")
# person2 = Person("Austin")
# person3 = Person("Kimberly")



# person1.talks()
# person2.talks()
# person3.talks()


        
class BankAccount:
    def __init__(self,account_number,balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit aamount")


    def withdraw(self,amount):
        if amount > 0:
            if self.balance <= amount:
               print("Insufficient balance")
            else:
                self.balance -= amount
        else:
            print("Invalid withdraw sum")


    def display_info(self):
        print(f"Account Number: {self.account_number} || Name: {self.owner} || Balance: {self.balance}")

    
   
account1 = BankAccount("12345",1000,"Mark")
account2 = BankAccount("23456",0,"Joyce")

account1.deposit(3000)
account1.withdraw(500)
account1.display_info()





    
     
        





