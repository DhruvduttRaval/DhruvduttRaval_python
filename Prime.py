n = int(input("ENTER N :"))

if n%2==0 :
    print (n , "is Not Prime")

else :
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print (n , "is Not Prime")
            break
    else :
        print (n ,"is Prime")



