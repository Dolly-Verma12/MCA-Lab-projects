Num1=int(input("Enter First Number: "))
op=input("Enter Operator: ")
Num2=int(input("Enter Second Number: "))
print()
if(op=='+'):
    print("Result: ",Num1+Num2)
elif(op=='-'):
    print("Result: ",Num1-Num2)
elif(op=='*'):
    print("Result: ",Num1*Num2)
elif(op=='/'):
    print("Result: ",Num1/Num2)
else:
    print("Invalid Operator!!")