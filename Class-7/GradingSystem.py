print("Enter marks obtained in 5 subjects")

sub1=int(input("Subject1"))
sub2=int(input("Subject2"))
sub3=int(input("Subject3"))
sub4=int(input("Subject4"))
sub5=int(input("Subject5"))

total=(sub1+sub2+sub3+sub4+sub5)
average=total/5

if(average>=81 and average<=100):
    print("Your Grade is A")

elif(average>=61 and average<81):
    print("Your Grade is B")

elif(average>=41 and average<61):
    print("Your Grade is C")

elif(average>=31 and average<41):
    print("Your Grade is D")

elif(average>=0 and average<31):
    print("FAIL")

else:
    print("Invalid Input")