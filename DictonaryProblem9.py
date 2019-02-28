# 9. Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name

# import itera

people={'Arham':'Blue', 'Lisa':'Yellow', 'Vinod': 'Purple' , 'Jenny':'Pink' }

def Dictionary():
    print("The dictonary is {}".format(people))
    print()
    # print(people.__len__())
    print("The number of the students in the dictonary is : {}".format(len(people.keys())))
    print()
    people['Lisa'] = "Red"
    print("{}  The Lisa's favourite color is now changed to {}".format(people,people["Lisa"]))
    print()
    people.pop("Jenny")
    print("The dictonary after removing Jeeny's record is {}".format(people))
    print()
    print("The dictonary after sorting on key is  ")
    for key in sorted(people.keys()):
        print("{} : {} ,".format(key, people[key]),end=" " )





Dictionary()
