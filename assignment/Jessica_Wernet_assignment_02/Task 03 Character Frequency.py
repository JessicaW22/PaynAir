string = input()
string = string.replace(" ", "")
print(string)

stringSet = set(string) 
def countCharacterFrequency(string):
        frequency = {} 
        for i in stringSet:
           frequency[i] = string.count(i) 
        return frequency

print(countCharacterFrequency(string))