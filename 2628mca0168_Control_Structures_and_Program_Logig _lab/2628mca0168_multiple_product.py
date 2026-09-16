number_of_products = int(input("Enter number of products: "))

total = 0

for i in range(number_of_products):
    price = float(input(f"Enter price of product {i + 1}: ₹"))
    total += price

if total < 1000:
    discount_rate = 0
elif total < 5000:
    discount_rate = 5
elif total < 10000:
    discount_rate = 10
else:
    discount_rate = 15

discount_amount = total * discount_rate / 100
final_amount = total - discount_amount

print("\n--- BILL SUMMARY ---")
print("Total Amount: ₹", total)
print("Discount:", discount_rate, "%")
print("Discount Amount: ₹", discount_amount)
print("Final Amount: ₹", final_amount)