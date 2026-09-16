customer_name=input("Enter your name: ")
cust_membership=input("Enter membership type (Regular\Premium\VIP): ")
purchase_Amount=float(input("Enter Purchase Ammount: "))
Discount=0
if purchase_Amount<=1000.0:
    Discount=0
elif purchase_Amount>1000.0 and purchase_Amount<5000.0:

    Discount=0.5
elif purchase_Amount<=5000.0 and purchase_Amount<10000.0:

    Discount=0.10
else:
    Discount=0.15

if cust_membership.lower()=="premium":
    Discount+=0.5
elif cust_membership.lower()=="vip":
    Discount+=0.10
else:
    Discount=Discount
discount_Amount=purchase_Amount*Discount/10
final_Amount=purchase_Amount-discount_Amount
print("------Bill Summary-------")
print("Total Amount : ",purchase_Amount)
print("Customer Membership",cust_membership)
print("Discount Rate: ",Discount ," %")
print("Discount Amount: ",discount_Amount)
print("Final Amount: ",final_Amount)