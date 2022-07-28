import UDF
sname=input("Enter Your Name : ")
d=open(sname,"w")
d.write(" ")
d.close()
d=open(sname,"a")
while True:

    print("*"*50)
    print("1.OddEven")
    print("2.MaxOfTwo")
    print("3.MaxOfThree")
    print("4.Fibonacci")
    print("5.Prime")
    print("6.Pattern")
    print("7.Exit")
    print("*"*50)
    choice=int(input("Enter Your Choice :"))
    print("*"*50)


    if choice==1:
        a =int(input("Enter Value :"))
        UDF.OddEven(a)
        d.write("\n You Opted OddEven Function")
        print("You Opted OddEven Function")
        print("*"*50)

    elif choice==2:
        a=int(input("Enter Value :"))
        b=int(input("Enter Value :"))
        UDF.MaxOfTwo(a,b)
        d.write("\n You Opted Maxoftwo Function")
        print("You Opted Maxoftwo Function")
        print("*"*50)

    elif choice==3:
        a=int(input("Enter Value :"))
        b=int(input("Enter Value :"))
        c=int(input("Enter Value :"))
        UDF.MaxOfThree(a,b,c)
        d.write("\n You Opted Maxofthree Function")
        print("You Opted Maxofthree Function")
        print("*"*50)

    elif choice==4:
        a=int(input("Enter Value :"))
        UDF.Fibonacci(a)
        d.write("\n You Opted fibonacci Function")
        print("You Opted fibonacci Function")
        print("*"*50)

    elif choice==5:
        a=int(input("Enter Value :"))
        UDF.Prime(a)
        d.write("\n You Opted prime Function")
        print("You Opted prime Function")
        print("*"*50)

    elif choice==6:
        a=int(input("Enter Value :"))
        UDF.Pattern(a)
        d.write("\n You Opted pattern Function")
        print("You Opted pattern Function")
        print("*"*50)

    else :
        print("Thank You.Good By")
        break

d.close()

d=open(sname,"r")
print(d.read())
d.close()