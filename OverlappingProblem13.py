# 13. Define a function overlapping() that takes two lists and returns True if they have at least one
# member in common, False otherwise.

def Overlapping():
    String1  = input("  Enter the List1  : ")
    String2  = input("  Enter the List2  : ")
    isContain = False
    List1 = list(String1.split(" "))
    List2 = list(String2.split(" "))
    commonList = []
    for value in List1:
        if List2.__contains__(value):
            isContain = True
            commonList.append(value)
    if isContain  == True:
        print(" List1 and List2 have members in common . Common member list is {} ".format(commonList))
    else:
        print(" List1 and List2 does not have members in common ")

Overlapping()
