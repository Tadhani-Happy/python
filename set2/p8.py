a = int(input("enter 1st no.:"))
b = int(input("enter 2nd no.:"))
op = input("enter sign of operation form given belloww: \n + \n - \n * \n / \n")
match op:
    case "+":
        print(a+b)
    case "-":
        print(a-b)    
    case "*":
        print(a*b)
    case "/":
        print(a/b)    
    case _:
        print("not valid operation! try again ")    