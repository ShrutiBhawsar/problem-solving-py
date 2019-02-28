# 14. Write a function find_longest_word() that takes a list of words and returns the length of the
# longest word and that word itself.


def find_longest_word():
    input_string = input("Enter the list of words :" )
    ListString = list(input_string.split(" "))
    ListString.sort(key = len , reverse= -1)
    # print(ListString)
    print("Longest word in the list is {} ".format(ListString[0]))

find_longest_word()

