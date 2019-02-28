def Histogram():
    HesString = input(" Enter the list of numbers  less than 20 : ")
    HesList =list(HesString.split(" "))    # spliting the string numbers in list
    # print(HesList)
    for value in HesList:            #for every number in the list
        # print(value)
        Histo= list(range(0,int(value)))   #creating the list of n number 
        for i in Histo:
            print("*" , end=" ")
        print()

Histogram()