n = int(input("enter a number:"))
c = 0
print(type(n))
while n != 0:
     d = n / 10
     n = int(d)
     c += 1

print("number of digitd are",c)