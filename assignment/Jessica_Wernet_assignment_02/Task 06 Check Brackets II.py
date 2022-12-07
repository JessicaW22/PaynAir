input("Pls enter a mathematical expression:")

string = input()
boo = False
for i in string:       
    if i not in "([{}])":
        string =string.replace(i ,"")        
string_2 = ""

while string_2 != string:
    string_2 =string
    string =string.replace("()","")
    string =string.replace("[]","")
    string =string.replace("{}","")
    
if string == "":
    print("Correct input")
else:
    print("Wrong input")