amount = int(input("Enter amount for withdrawl"))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10

print("100 rupee note: ",note_1)
print("50 rupee note: ",note_2)
print("10 rupee note: ",note_3)