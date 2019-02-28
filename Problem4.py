#Write a program that asks the user how many days are in a particular month, and what day of the
# week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for that
# month. For example, here is the output for a 30-day month that begins on day 4 (Thursday):
# S M T W T F S
# 1 2 3
# 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30


week = [ "Su", "Mo", 'Tu', "We", "Th", "Fr", "Sa"]

days30 = list(range(1, 30+1))
days31 = list(range(1 , 31 + 1))
# daystring = " ".join(week)
# print(daystring)



def calender():
    input_No_of_days =  input(" Enter the number of days in a particular month (30/31/28) : " )
    print("select - 0 for Sunday ,1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday, 6  for Saturday,")
    input_day_of_week = input(" Enter the day of the week the month begins on ( 0 to 6 ) : ")
    start_pos = int(input_day_of_week)
    daystring = " ".join(week)       # converting week list to string
    print(daystring)
    spacing = list(range(0,start_pos))     #providing spacing till the first day of the week
    for space in spacing:
        print("{:>2}".format(""), end = " ")

    if input_No_of_days == "30":
        days = days30
    else:
        days = days31

    for day in days:
        print('{:>2}'.format(day), end=' ')
        start_pos += 1
        if start_pos ==7:
            # If start_pos == 7 (Sunday) start new line
            print()
            start_pos = 0      # Reset counter
    print('\n')


calender()