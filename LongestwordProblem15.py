# 15.Write a function filter_long_words() that takes a list of words and an integer len and returns the
# list of words that are longer than len.

input_string = input(" Please enter the list of words :   ")
input_length = input(" Please enter the length   ")

def filter_long_words(word):
    if len(word) > int (input_length):
        # print(word)
        # print (len(word))
        return word


def main_function():
    liststring = list(input_string.split(" "))    # string is converted to list of strings
    print(input_string)
    print(liststring)
    listWords = list(filter(filter_long_words, liststring))
    print("List of strings which has their length greater than {} is {} ".format(input_length, listWords))


main_function()

