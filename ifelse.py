
#MARK PROGRAM TEST
"""
mark = int(input("What is your mark?:"))

####### Start of if, elif, else function#######
if mark >= 85:            # >= equal or greater than 85
    print("Distinction")
elif mark >= 65:          # >= equal or greater than 65
    print("Pass")         # will print "Pass"
else:
    print("Failed")       # will print "Failed"
"""
    """End of function, Stretchs from first 3 commas to last 3 commas"""

    """print(__doc__) prints whatever documents there are"""


#GRADE CALCULATOR
"""
print('Welcome to Grade Calculator')
print()
print("Please enter your maths mark:")
maths_mark = int(input())
print("Please enter your chemistry mark:")
chemistry_mark = int(input())
print("Please enter your physics mark:")
physics_mark = int(input())
total_mark = maths_mark + chemistry_mark + physics_mark
print('Here is the total mark : ', total_mark)
print()
percentage_mark = int((total_mark) / 3)
print('Here is the Percentage mark : ', percentage_mark)
print()

if percentage_mark >= 70:
    print("A")
elif percentage_mark >= 60 and percentage_mark < 70:
    print("B")
elif percentage_mark >= 50 and percentage_mark < 60:
    print("C")
elif percentage_mark >= 40 and percentage_mark < 50:
    print("D")
else:
    print("Failed")
"""

"""This is a simple program to demonstrate comparators and if statements"""
bank_total = 300
deposit_money = 40
withdraw_money = 160

if deposit_money > 0:
    new_total = bank_total + deposit_money
    bank_total = new_total
    print("New bank total = £", bank_total)
else:
    print("Invalid deposit total")

if withdraw_money <= bank_total:

    if withdraw_money >= 0:
        new_total = bank_total - withdraw_money
        print("After Withdrawing £", withdraw_money, "the new total is £", new_total)
    else:
        print("invalid withdraw amount")
""""""