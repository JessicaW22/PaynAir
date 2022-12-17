#1. Write a function that spans a dictionary holding a default balance of 0 for an initial list of customers. For simplicity, assume customer names are unique identifier. 
customers = {'Hughie': 0, 'Lewie': 0, 'Dewie': 0}

print(customers['Hughie']) 
print(customers['Lewie']) 
print(customers['Dewie']) 

#2. What are elegant ways to add or remove single and multiple customers using the functionality of dict?

#remove single customer

del customers['Hughie']
print(customers)

#remove all customers

customers.clear()
print(customers)

#add single/multiple customers
customers = {'Lillie': 0, 'Millie': 0}
print(customers)

#3. Now write two simple functions that allow you to deposit and withdraw money for a given bank customer.
#4. Include error messages for inputs that are not permissible, e.g., withdrawing negative amounts or overdrawing the account, etc.

def deposit(customer, payment):
    if payment < 0:
        print("You can't deposit negative money.")
    else:
        customers[customer] += payment
    

def withdraw(customer, withdrawal):
    if withdrawal < 0:
        print("You can't withdraw negative money.")
    elif customers[customer]<withdrawal:
        print("Your account balance is not high enough for the requested withdrawal")
    else:
        customers[customer] -= withdrawal

deposit('Millie', -1)
print(customers)
deposit('Millie', 5)
print(customers)
withdraw('Millie', 2.5)
print(customers)
withdraw('Millie', 100)
print(customers)
withdraw('Millie', -5)
print(customers)