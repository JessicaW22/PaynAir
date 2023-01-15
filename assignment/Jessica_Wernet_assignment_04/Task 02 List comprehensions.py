def remove_long_words(s, n):

    word_list = s.split()
    print("Input")
    print(word_list)
    word_list_new = []

    for x in word_list:
        if len(x)>n:
            continue
        else:
            word_list_new.append(x)

    print("Output")
    print(word_list_new)

myInput = input("Enter a sentence")
myInput2 = int(input("Enter a word length"))
remove_long_words(myInput, myInput2)