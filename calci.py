#simple calculator!
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Invalid!!")
def divint(x,y):
    try:
        return x//y
    except ZeroDivisionError:
        print("Invalid!!")
n1=float(input("enter number1:"))
n2=float(input("enter number2:"))
print("click for options!!!\n")
print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.INTEGER DIVISION\n")
res=int(input("enter your choice:"))
if(res==1):
    print("Thr result is:",add(n1,n2))
elif(res==2):
    print("The result is:",sub(n1,n2))
elif(res==3):
    print("The result is:",multiplication(n1,n2))
elif(res==4):
    print("The result is:",div(n1,n2))
elif(res==5):
    print("The result is:",divint(n1,n2))
else:
    raise ValueError       
    













