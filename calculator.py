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
        x=log(b)
        result=0.0
        s=1.0
        for i in range(0,150):
            for i in range(0,i):
                
                
            result=result+
            
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
                    Enter 3 for linear equation with 3 variables"""))
    if(ch==1):
        print("For your linear equation of the form ax+b")
        a=input("Enter a")
        b=input("Enter b")
        x= -b/a
        print("x=",x)
    elif(ch==2):
        print("For your first linear equation in the form a1x+b1y+c1=0")
        a1=float(input("Enter a1"))
        b1=float(input("Enter b1"))
        c1=float(input("Enter c1"))
        print("For your second linear equation in the form a2x+b2y+c2=0")
        a2=float(input("Enter a2"))
        b2=float(input("Enter b2"))
        c2=float(input("Enter c2"))
        x= ((b2*c1)-(b1*c2))/((b1*a2)-(b2*a1))
        y= ((a2*c1)-(a1*c2))/((b2*a1)-(b1*a2))
        print("x=",x)
        print("y=",y)
    elif(ch==3):
        print("For your first linear equation in the form a1x+b1y+c1z=d1")
        a1=float(input("Enter a1"))
        b1=float(input("Enter b1"))
        c1=float(input("Enter c1"))
        d1=float(input("Enter d1"))
        print("For your second linear equation in the form a2x+b2y+c2z=d2")
        a2=float(input("Enter a2"))
        b2=float(input("Enter b2"))
        c2=float(input("Enter c2"))
        d2=float(input("Enter d2"))
        print("For your third linear equation in the form a3x+b3y+c3z=d3")
        a3=float(input("Enter a3"))
        b3=float(input("Enter b3"))
        c3=float(input("Enter c3"))
        d3=float(input("Enter d3"))
        D=(a1*(b2*c3-b3*c2))-(b1*(a2*c3-a3*c2))+(c1*(a2*b3-a3*b2))
        Dx=(d1*(b2*c3-b3*c2))-(b1*(d2*c3-d3*c2))+(c1*(d2*b3-d3*b2))
        Dy=(a1*(d2*c3-d3*c2))-(d1*(a2*c3-a3*c2))+(c1*(a2*d3-a3*d2))
        Dz=(a1*(b2*d3-b3*d2))-(b1*(a2*d3-a3*d2))+(d1*(a2*b3-a3*b2))
        if(D!=0):
            x=Dx/D
            y=Dy/D
            z=Dz/D
            print("x="+x)
            print("y="+y)
            print("z="+z)
        elif(D==0 and Dx==0 and Dy==0 and Dz==0):
            print("There are infinite solutions to this equation")
        elif(D==0 and (Dx!=0 or Dy!=0 or Dz!=0)):
            print("There are no solutions to this equation")
        else:
            print("Wrong input")
    else:
        print("Wrong input")
        
if(ch==6):
    print("For your quadratic equation in the form ax^2+bx+c")
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=int(input("enter c"))

    if((b**2)-(4*a*c))>=0:
        D1=((((b**2)-(4*a*c))**0.5) - b)/(2*a)
        D2= -((((b**2)-(4*a*c))**0.5) + b)/(2*a)
        print("The answers are=",D1,"or",D2)
    else:
        D1= (((4*a*c)-(b**2))**0.5) 
        D2= - (((4*a*c)-(b**2))**0.5) 
        print("The answers are =",-b/2,"+",D1/2,"i and",-b/2,"+",D2/2,"i")

