# Leap year is exactly divisible by 400 and 100 
# if considering century years then it should be divisible by 4 but not by 100

year=int(input("Enter an year to check:"))
if(year%400==0):
    print("Leap year")
elif (year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("Not a leap year")