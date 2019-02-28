#3. Accept the full name from user(Name Middlename Surname) in lowercase and Print it in title
# case. NOTE:(Using in-built function and User-defined function)


def Title():
    fullName = input("Enter your full name (Name Middlename Surname) in lower case :  ")
    print(" Using build-in function , title of name is  {}".format(fullName.title()))

    wordList = list(fullName.split(sep =" "))
    # print(wordList)
    print("Using user define function , title of name  is  :")
    for word in wordList:
        charList = list(word)         #converting each word into a character
        i = charList[0]      # taking 1st charater of the given character list
        if ord(i) >= 97 | ord(i) <=122:
            UpChar = chr (ord(i) - ord('a') + ord('A'))   # ord give ascii value  ,formula for Upper case
            charList[0] = UpChar                         #replacing the lower case char to upper case char
        newWord = "".join(charList)           #joining the char list to form a string
        print(newWord, end=" ")



Title()