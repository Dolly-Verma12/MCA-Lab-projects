Product_name=input("Enter Product Name: ")
Courrent_stock=int(input("Enter Your Courrent Stock: "))
Reorder_level=int(input("Enter Reorder level: "))
if(Courrent_stock==0):
    status="Out Of Stock!!"
    
elif(Courrent_stock<Reorder_level):
  status="Reorder Require!!"
else:
  status="Stock Available!!"
print()
print("====Inventry System====")
print("Product Name: ",Product_name)
print("Current Stock: ",Courrent_stock)
print("Reorder Level: ",Reorder_level)
print("Ststus: ",status)

