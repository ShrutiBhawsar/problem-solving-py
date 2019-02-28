# 12. Write a function sum() to add 1 to 10 numbers recursively.


def  RecursiveAdd(num):
    print("{} + ".format(num),end="")

    if num == 1:
        return num+1;
    else:
        return num + RecursiveAdd(num-1)



sum = RecursiveAdd(10)
print()
print(sum)


