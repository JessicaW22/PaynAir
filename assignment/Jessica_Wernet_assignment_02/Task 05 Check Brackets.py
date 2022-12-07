string = input("Pls enter a mathematical expression:")

def check_brackets(string):
    counter = 0
    for i in string:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1

    if counter == 0:
        return True
    else:
        return False

print(check_brackets(string))