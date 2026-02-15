# Student Grade Calculator

name = input("Enter Name:")

sub1_mark = float(input("Enter marks for subject 1:"))
sub2_mark = float(input("Enter marks for subject 2:"))
sub3_mark = float(input("Enter marks for subject 3:"))

if (0 <= sub1_mark <= 100) and (0 <= sub2_mark <= 100) and (0 <= sub3_mark <= 100):
    total = sub1_mark + sub2_mark + sub3_mark
    percentage = (total/300)*100

    if percentage >= 75:
        grade ="A"
    elif percentage >= 60:
        grade ="B"
    elif percentage >= 40:
        grade ="C"
    else:
        grade ="F"

    print("\n", name)
    print("Total:",total,"/300")
    print("Percentage:",round(percentage,2),"%")
    print("Grade:",grade)
else:
    print("Error!")