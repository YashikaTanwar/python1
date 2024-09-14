actual_cost=float(input("Enter actual cost of the product:"))
sale_amount=float(input("Enter actual sale amount of the product:"))
if(sale_amount>actual_cost):
    profit=sale_amount-actual_cost
    print("Total profit ",profit)
else:
    print("No profit")