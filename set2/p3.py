n= int(input("enter a number:"))
print("all digits are:")
while  n != 0 :
     p = n % 10
     d = n / 10
     n = int(d)
     print(p)
