while True:
    n = input("enter a number:")

    if n == "":
        break
    n= int(n)
    if n < 0:
        print("no. is negative:",n)
    elif n >= 0 :
        print("no. is positive:",n)