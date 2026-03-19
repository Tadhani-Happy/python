a = int(input("enter integer a:"))
b = int(input("enter integer b:"))
print("all the even no. between a and b are:")

while a <= b:
    if a % 2 == 0:
        print(a)
    a +=1

for a in range(a, b):
    if a % 2 == 0:
        print(a)