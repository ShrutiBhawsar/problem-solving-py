# 8. In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in
# the plain text is replaced by a letter some fixed number of positions down the alphabet. For
# example, with a shift of 3, A would be replaced by D, B would become E, and so on. The method
# is named after Julius Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13
# places") is a widely used example of a Caesar cipher where the shift is 13. In Python, the key for
# ROT-13 may be represented by means of the following dictionary:
# key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a',
# 'o':'b','p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P',
# 'D':'Q', 'E':'R','F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A','O':'B', 'P':'C', 'Q':'D',
# 'R':'E', 'S':'F', 'T':'G','U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
# Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're done, you
# will be able to read the following secret message:
# Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
# Note that since English has 26 characters, your ROT-13 program will be able to both encode and
# decode texts written in English.


Cryptokey = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a',
'o':'b','p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P',
'D':'Q', 'E':'R','F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A','O':'B', 'P':'C', 'Q':'D',
'R':'E', 'S':'F', 'T':'G','U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

def cryptography(word):
    """
    it take word from the iterator map and check for each character in word and replace it with the character in the dictonary
    and concatinate replaced char to  the string
    :param word:
    :return: string( word)
    """
    finalword = ""
    for character in word:
        if character in Cryptokey:
            finalword = finalword + str(Cryptokey.get(character))
        else:
            finalword = finalword + character

    return finalword



def main_Funtion():
    input_isEncDec = input(" Do you want to Encode or Decode ( Give 'E' for encode , 'D' for Decode ) :" )
    if input_isEncDec.isalpha():
        if input_isEncDec == 'E':
            input_string = input(" Enter the text to Encode : ")
            EncodewordList = list(input_string.split(" "))    # list of words
            # print(EncodeList)
            #calling cryotography on the list of words in EncodewordList
            finalList = list(map(cryptography , EncodewordList))  # words will be passed to cryptography function
        elif input_isEncDec == 'D':
            input_string = input(" Enter the text to decode : ")
            DecodewordList = list(input_string.split(" "))
            # print(EncodeList)
            finalList = list(map(cryptography , DecodewordList))
        else:
            print(" oopss!!!You entered the wrong option. Enter the right option E/D ")
            return

        finalSting = " ".join(finalList)     #joining the list of words to form a string
        print(" The result is '{}' ".format(finalSting))


main_Funtion()












