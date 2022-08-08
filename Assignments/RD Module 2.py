#1) if a number is positive, negative or zero

x = int (input ("Enter a number :"))

if x<0 :
    print ("number is negative")

elif x==0 :
    print ("number is zero")

else :
    print ("number is positive")

#2) get the Factorial number
a = int(input("Enter a Number :"))
factorial = 1
while (a>0):
   factorial = factorial * a
   a=a-1
print("The Factorial of The Number is : ")
print(factorial)

#3) get the Fibonacci series

n=int(input("Enter N : "))
a,b=0,1
print(a,end=" ")
while b<n:
    print(b,end=" ")
    a,b=b,a+b
      
#6) swap two number :-
#without temp variable ,

x = 10 
y = 20 
x,y = y,x
print ('x=',x)
print ('y=',y)

#with temp variable ,

x = 10
y = 20

temp = x
x = y 
y = temp 


print ('value of x:{}'.format(x))
print ('value of y:{}'.format(y))

# 7) even or odd number :-

a = int(input("Enter a number: "))
x = a % 2
if x > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

# 8) vowel or not :-

x = input("Enter a single character :")

if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" :
    print("Character is vowel")
else :
    print("Character is not vowel")

# 9) three given integers.
    # ,if two values are equal sum will be zero.

a = int(input("ENTER NUMBER A:"))
b = int(input("ENTER NUMBER B:"))
c = int(input("ENTER NUMBER C:"))

if a==b or b==c or c==a:
    print("Sum of value is zero")
else :
    print("sum of value is :" , a+b+c)

# 10) first n positive integers :-

n = int(input("enter a number: "))
x = (n * (n + 1)) / 2
print("Sum of the first", n)
 
if n>0:
    print ("positive integers:", x)
else :        
    print ("negative integers:", -x)

#11) length of string :-

x = input("Enter a string :")
print (len(x))

#12) count the number of characters :-

#
x = str(input("Enter a name :"))
b = str(input("Enter a character :"))

print (x.count(b))


#method 2 :-
a = input("Enter a String :")
b = 0
for i in a :
    if i.isalnum():
        b=b+1
print("Total Number Of Characters :",b)

#13)count occurrences of a substring in a string.

x = str(input("Enter a name :"))
b = str(input("Enter a character :"))

print (x.count(b))

#14)count the occurrences of each word


a = ("Tops Technologies Institute")
b = 0

for i in a :
   if i.isalnum():
     b=b+1
print(b)

#15)swap the first two characters of each string.

a = input("Enter a String :")
b = input("Enter a String :")
c = a[0:2] + b[2:]
d = b[0:2] + a[2:]

print(c,d)

#16)add 'ing' at the end of a given string.

a=input("Enter a String :")
if len(a)<=3:
    print(a)
elif a.endswith('ing'):
    print(a +"ly")
else:
    print(a +'ing') 

#17)find the first appearance of the substring 'not' and 'poor' from a given string.

s="Karan's condition is not poor."
print(s.replace(s[(s.find('not')):((s.find('poor'))+4)], 'good'))

#18)a list of words and returns the length of the longest one.

a=['Dhruvdutt', 'Abcd', 'Fruits', 'Foods']
def fun(a):
    b=[]
    for i in a:
        b.append(len(i))
    print(max(b))
fun(a)

#19)a Python function to reverses a string if its length is a multiple of 4.

b= input("Enter a string: ")
def fun(a):
    if len(a)%4==0:
        for i in a[::-1]:
            print(i, end='')          
    else:
        print(a)
fun(b)

#20)a Python program to get a string made of the first 2 and the last 2 chars from a given a string


a= input("Enter a string: ")
if len(a)<2:
    print("Empty string")
elif len(a)==2:
    print(a*2)
else:
    print(a[0:2]+a[(len(a)-2):])


#21)a Python function to insert a string in the middle of a string.

a="Tops Technologies"
b=input("Enter a Substring: ")
n=int(input("Enter number at which you want to change: "))
print(a[:n],b+a[n:])





