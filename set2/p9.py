'''def is_prime(n): #function for prime number  # manual laber work
    if n%2==0:
        if n==2:
            print(n,"is prime no.")
        else :    
            print(n,"not a prime no. is divisable by 2")
    elif  n%3==0:
        if n==3:
            print(n,"is prime no.")
        else :    
            print(n,"not a prime no. is divisable by 3")
    elif  n%5==0:
        if n==5:
            print(n,"is prime no.")
        else :    
            print(n,"not a prime no. is divisable by 5")
    elif  n%7==0:
        if n==7:
            print(n,"is prime no.")
        else :    
            print(n,"not a prime no. is divisable by 7")
    else:
        print(n,"is a prime number")
'''

n= int(input("enter a no.:"))
#is_prime(n)

def prime(n):   # smart loop 
    count =0
    for i in range(2,8):
        if n%i==0 and i!=n:
            count +=1
    if count==0:
            print(n,"is prime")
    else :
            print(n,"is not a prime")

prime(n)