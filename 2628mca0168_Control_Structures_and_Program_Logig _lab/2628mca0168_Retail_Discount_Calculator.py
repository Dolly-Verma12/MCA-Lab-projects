
customer_name=input("Enter Customer Name: ")
purchase_Amount=float((input("Enter purchase Amount: ")))

if purchase_Amount<=1000.0:
    Discount=0
elif purchase_Amount>1000.0 and purchase_Amount<5000.0:

    Discount=0.5
elif purchase_Amount<=5000.0 and purchase_Amount<10000.0:

    Discount=0.10
else:
    Discount=0.15
discount_Amount=purchase_Amount*Discount/10
finalAmount=purchase_Amount-discount_Amount
print()

print("------Bill Summary-------")
print("Total Amount : ",purchase_Amount)
print("Discount Rate: ",Discount ," %")
print("Discount Amount: ",discount_Amount)
print("Final Amount: ",finalAmount)
