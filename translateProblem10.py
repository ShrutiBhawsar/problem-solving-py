# 10.Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's
# language"). That is, double every consonant and place an occurrence of "o" in between. For
# example, translate("this is fun") should return the string "tothohisos isos fofunon".

Vowels_Space_Tuple = ('a' ,'e','i','o','u',' ')

def translate(character):
    """
    it is taking each character from the strinlist and comaring it with vowel and space.
    if the character is consonant , it will return the string which is created by concatination of character with 'o'
    else it will return the vowel/space
    :param character: it is the character from the iterator of map function
    :return: returns the concatinated string
    """
    subString = ""
    if character not in Vowels_Space_Tuple:
        subString = character  + "o" + character
    else:
        subString = character

    return subString

def main_function():
    input_String = input("Please enter a sentence to be translated : ")
    charList     = list(input_String)
    # print(charList)
    translatedCharList = list(map(translate,charList))
    translatedString = "".join(translatedCharList)
    print(" The translation of '{}' is '{}' ".format(input_String,translatedString))


main_function()