Num=int(input("Enter Number: "))
def greet(Num):
    while Num>1:
        greet(Num)*greet(Num-1)
    
print(greet(Num))