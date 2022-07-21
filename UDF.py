def OddEven(a):
    if a%2==0:
        print(a,"is Even")
    else:
        print(a,"is Odd")

def MaxOfTwo(a,b):
    if a>b:
        print(a,"is Max")
    else:
        print(b,"is Max")

def MaxOfThree(a,b,c):
    if a>b:
        if a>c:
            print(a,"is Max")
        else:
            print(c,"is Max")
    elif b>c:
        print(b,"is Max")
    else:
        print(c,"is Max")

def Fibonacci(n):
    a,b=0,1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()

def Prime(a):
    if a%2==0:
        print(a,"is Not Prime")
    else:
        for i in range(3,int(a/2)+1,2):
            if a%i==0:
                print(a,"is Not Prime")
                break
        else:
            print(a,"is Prime")

def Pattern(n):
    for i in range(1,n+1):
        print("*"*i)


#read moduledemo.py file


  
        


