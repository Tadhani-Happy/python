import random
i = int(random.randint(1,10))
while True:
    n = int(input("guess a number btw 1-10:"))
    if n== i:
        print("congatulations, you won")
        break
    elif n > i:
        print("high")
    else :
        print("low")