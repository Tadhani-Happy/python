p = int(input("enter principle amount:"))
r = int(input("enter rate:"))
t = int(input("enter time:"))
Int= (p * r*t)/100
print("intrest=",Int ,"rupyes\n", type(Int))
tm= p+ Int
print("total amount=", tm)