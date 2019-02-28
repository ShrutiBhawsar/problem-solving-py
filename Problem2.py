#2. Print the given number in words.(eg.1234 => one two three four).


def NumberToWords(digit):
    # dig = int(digit)
    """
    It contains logic to convert the digit to word
    it will return the word corresponding to the given digit
    :param digit: It should be integer
    :return: returns the string back
    """

    digitToWord = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven',
                   8: 'Eight', 9: 'Nine'}

    return digitToWord.get(digit, " Not Valid")


def NumberInWords():
    """
    This is the main function.We are getting the input(Number) in string
    String is converted to list and each digit is passded to NumberToWords function
    :param numInString: Number string
    :return: it returns nothing
    """
    numInString = input("Please enter the number :  ")
    if numInString.isnumeric():
        print("The Number to word convertion for {} is : ".format(numInString))
        number = list(numInString)
        for digit in number:
            word = NumberToWords(int(digit))
            print(word, end= " ")
        print()
    else:
        print("Wrong input!!..Please enter the number only")



NumberInWords()

