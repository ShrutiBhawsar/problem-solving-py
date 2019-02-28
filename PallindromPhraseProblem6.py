#Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go
# hanga salami I'm a lasagna hog.", "


#maketrans() function is used to construct the transition table i.e specify the list of characters that need to be
# replaced in the whole string or the characters that need to be deleted from the string


import string

def PhrasePallindrom():
    phrase = input("Enter a phrase : ")
    table = phrase.maketrans("","", string.punctuation)   #removing the punctuations from the string
    phraseNoPunct = phrase.translate(table)
    print(phraseNoPunct)
    phraseNoSpace = phraseNoPunct.replace(" ","")
    print(phraseNoSpace)
    print("Original phrase is  : {}".format(phraseNoSpace.lower()))

    # reversing the string
    phraseList = list(phraseNoSpace)
    phraseList.reverse()
    ReversedPhrase = "".join(phraseList)
    print("Reversing the phrase  {} ".format(ReversedPhrase.lower()))

    if phraseNoSpace.lower() == ReversedPhrase.lower():
        print("The given phrase is pallindrome  ")
    else:
        print("The given phrase is NOT pallindrome  ")



PhrasePallindrom()