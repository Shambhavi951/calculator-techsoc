print("CALCULATOR")
print("Enter the task which you want to perform")
choice=int(input("""Enter 1 for arithmetic functions
                    Enter 2 for trigonometric functions
                    Enter 3 for exponential function
                    Enter 4 for logarithmic functions
                    Enter 5 for linear equation solver
                    Enter 6 for quadratic equation solver
                    """))
if(choice==1):
    def add(a,b):
        return(a+b)
    def subtract(a,b):
        return(a-b)
    def multiply(a,b):
        return(a*b)
    def divide(a,b):
        return(a/b)

#main
    ans='y'
    while(ans=='y'):
        op=input("Enter the arithmetic operation you wish to perform(addition/subtraction/multiplication/division)")
        if(op=="addition"):
            a=float(input("Enter the first number"))
            b=float(input("Enter the second number"))
            result=add(a,b)
        elif(op=="subtraction"):
            a=float(input("Enter the first number"))
            b=float(input("Enter the second number"))
            result=subtract(a,b)
        elif(op=="multiplication"):
            a=float(input("Enter the first number"))
            b=float(input("Enter the second number"))
            result=multiply(a,b)
        elif(op=="division"):
            a=float(input("Enter the first number"))
            b=float(input("Enter the second number"))
            result=divide(a,b)
        else:
            print("No valid option has been entered.Please try again")
            print("Result=",result)
        ans=input("Do you want to perform another operation(y/n)")

elif(choice==2):
    def factorial(n):
        fact=0.0
        if(n==0 or n==1):
            fact=1
        else:
            fact=n*factorial(n-1)
        return fact
    def sin(x):
        result=0.0
        for i in range(1,150,2):
            f=factorial(i)
            if (((i-1)/2)%2==0):
                result=result + (x**i)/f
            elif(((i-1)/2)%2!=0):
                result=result - (x**i)/f
        return result
    
    def cos(x):
        result=0.0
        for i in range(0,150,2):
            f=factorial(i)
        if((i/2)%2==0):
            result=result + ((x**i)/f)
        elif((i/2)%2!=0):
            result=result - ((x**i)/f)
        return result

    

    
#main
    x=int(input("Enter the angle in radians"))
    op=input("Enter the operation you want to perform (sin/cos/tan/sec/cosec/cot)")
    if (op=="sin"):
        ans=sin(x)
        print("Result=",ans)
    elif (op=="cos"):
        ans=cos(x)
        print("Result=",ans)
    elif (op=="tan"):
        ans=sin(x)/cos(x)
        print("Result=",ans)
    elif (op=="cosec"):
        ans=1/sin(x)
        print("Result=",ans)
    elif (op=="sec"):
        ans=1/cos(x)
        print("Result=",ans)
    elif (op=="cot"):
        ans=cos(x)/sin(x)
        print("Result=",ans)


elif(choice==3):
    def power():
        b=float(input("Enter the base"))
        e=int(input("Enter the exponent"))
        result=1
        if(e<0):
            for i in range(e):
                result=result*(1/b)
        else:
            for i in range(e):
                result=result*b
        print("Result=",result)
#main
    power()
    
elif(choice==4):
    def log():
        b=float(input("Enter the base of the log"))
        a=float(input("Enter the value of a in logb (a)"))
        n=newt(a)
        d=newt(b)
        ans=n/d
        print("Log value=",ans)
    
    def newt(n):
        e=2.718281828459045
        x=1.0
        f=(e**x)-n
        fd=e**x
        for i in range(1,150):
            x=x-((f)/(fd))
            f=(e**x)-n
            fd=e**x
        return x
    log()
    
elif(choice==5):
    ch=int(input("""Enter 1 for linear equation with 1 variable
                    Enter 2 for linear equation with 2 variables
                    Enter 3 for linear equation with 3 variable"""))

