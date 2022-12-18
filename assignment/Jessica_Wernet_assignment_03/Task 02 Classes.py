#The manager thinks that the simple bookkeeping system you have built is not powerful enough. She requests that you start from scratch and use classes instead.
#1. Write a simple class with appropriate constructor *__init__* that initializes an object of class *Customer* tracking the same information as in Task 01.
class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def show(self):
        print(f"Balance of {self.name}: {self.balance}")
        
#2.Now write two simple methods for class *Customer* that allow you to deposit and withdraw money for a given customer object.
#3.Include error messages for inputs that are not permissible, e.g., withdrawing negative amounts or overdrawing the account.
    
    #deposit money
    def deposit(self, amount):
        if amount < 0:
            print("\nYou can't deposit negative money.")
        else:
            self.balance += amount

    #withdraw money
    def withdraw(self, amount):
        if amount < 0:
            print("\nYou can't withdraw negative money.")
        elif self.balance < amount:
            print("\nYour account balance is not high enough for the requested withdrawal.")
        else:
            self.balance -= amount

#4.Inheritance: Write a child class *SavingsCustomer* that inherits its features from the parent class *Customer*. A savings customer has an extra savings balance for receiving extra interest. The class should have a method to transfer money back and forth between the accounts' main balance as well as the savings balance. Do not forget to add reasonable error messages.
class SavingsCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)
        self.savings_balance = 0

    #deposit savings
    def deposit_savings(self, amount):
        if amount > self.balance:
            print("\nYour account balance is not high enough for the requested withdrawal.")
        else:
            self.savings_balance += amount
            self.balance -= amount

    #withdraw savings
    def withdraw_savings(self, amount):
        if amount < 0:
            print("\nYou can't withdraw negative money.")
        elif self.savings_balance < amount:
            print("\nYour account balance is not high enough for the requested withdrawal.")
        else:
            self.savings_balance -= amount
            self.balance += amount

    #show current account balance
    def show_savings(self):
        print(f"Savings balance of {self.name}: {self.savings_balance}")


c1 = SavingsCustomer("Hughie")
c1.show()
c1.deposit(50)
c1.show()
c1.show_savings()
c1.deposit_savings(25)
c1.show()
c1.show_savings()
c1.withdraw_savings(30)