#calculator
print("enter\n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division")
def ad():
    x=int(input("enter the 1st oparand"))
    y=int(input("enter your nd oparand"))
    return x+y
def sb():
    x=int(input("enter the 1st oparand"))
    y=int(input("enter your nd oparand"))
    return x-y
def ml():
    x=int(input("enter the 1st oparand"))
    y=int(input("enter your nd oparand"))
    return x*y
def dv():
    x=int(input("enter the 1st oparand"))
    y=int(input("enter your nd oparand"))
    return x/y
a=int(input("enter what arthamatic operations ou want to perform"))
if a==1:
    p=ad()
    print("the result is=",p)
elif a==2:
    p=sb()
    print("the result is=",p)
elif a==3:
    p=ml()
    print("the result is=",p)
elif a==4:
    p=dv()
    print("the result is=",p)
else:
    print("enter the valid number")


    