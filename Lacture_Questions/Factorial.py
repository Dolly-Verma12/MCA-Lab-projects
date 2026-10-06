Num=int(input("Enter Number: "))
def factorial(Num):
     fact=1
     for i in range(1,Num+1):
          fact*=i
          
     return fact  

    
print(factorial(Num))