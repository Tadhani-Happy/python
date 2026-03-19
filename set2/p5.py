n = int(input("enter a number:"))
s = 0
print(type(n))
while n != 0:
     p = n % 10
     d = n / 10
     n = int(d)
     s += p

print("number of digitd are",s)