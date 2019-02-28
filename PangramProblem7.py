#7. A pangram is a sentence that contains all the letters of the English alphabet at least once, for
# example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to
# check a sentence to see if it is a pangram or not.

import string

Alphabets ='abcdefghijklmnopqrstuvwxyz'

def Pangram():
    sentence = input("Enter the sentence : ")
    ifPangram = True

    # table =sentence.maketrans("","",string.punctuation)
    # sentenceNoPunc = sentence.translate(table)
    for char in Alphabets:
        if char not in sentence:
            print("The character {} is not present in given sentence.So, the sentence is not a Pangram ".format(char))
            ifPangram = False
            break
    if ifPangram == True:
        print("The given sentence is a Pangram ")

Pangram()