#************MODULE :-3*****************RD-File.py


#1) list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

list1 = [2,33,222,14,25]
print(list1[-1]) 

#2)get the largest number, smallest num and sum of all from a list.

l1=[1,2,3,65,32,100,23,54,78,90]
def fun(l1):
    print("Largest Number :" , max(l1))
    print("Smallest Number :" , min(l1))
    print("Sum of All Number :" , sum(l1))
fun(l1) 

#3)count the number of strings

l1=['tops','technology','civic','trust','window','bathtub','erase','raval']
a=0

for i in l1:
    if len(i)>=2 and i[0]==i[-1] :
        a=a+1
print(a)

#4)program to remove duplicates from a list.

l=[1,1,2,5,6,7,8,5,1,7,10,4,6,10]
print(list(set(l)))

#5)program to check a list is empty or not.

a = []
if not len(a):
    print("list is empty")

#6)takes two lists and returns true if they have at least one common member.

l1=[1,2,3,4,5]
l2=[8,9,10,11,12]

for i in l1 :
    if i in l2:
        print('True')
        break
else :
    print('False')   

#7)first and last 5 elements where the values are square of numbers 
   # between 1 and 30.

l = []
for i in range(1,31):
		l.append(i**2)
p=(l[:5])
(p.extend(l[-5:]))
print(p)

#8)takes a list and returns a new list with unique elements of the first list.

def list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(list([1,2,3,3,3,4,4,5,1,2,1,4,6,9]))
 

#9)convert a list of characters into a string.

a=['D','H','R','U','V','D','U','T','T']
P=''.join(a)
print(P)

#10)program to select an item randomly from a list.

import random

p = [1, 'a', 32, 'c', 'd', 31,'b','e','f']
print(random.choice(p))

#11)program to find the second smallest number in a list.

l1=[1,2,3,4,5,6,7,8]
l1.sort()
print(l1[1])

#12)program to get unique values from a list

def list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(list([1,2,3,3,3,4,4,5,1,2,1,4,6,9]))

#13)program to check whether a list contains a sub list.

l=[]                  #if double [] then output is - contains sublists
for i in l:
    if type(i)==list:
        print("list contains sublist.")
        break
else:
    print("list does not contains sublist.")

#14)program to split a list into different variables.

color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
var1, var2, var3 = color
print(var1)
print(var2)
print(var3)

#15)program to create a tuple with different data types.

a=(1,2,3,1.1,4.5,True,"Dhruv",-45,100,"Python","language")
print(a) 

#16)program to create a tuple with numbers.

x=(1,3,67,90,100,34)
print(x) 

#17)program to convert a tuple to a string.

tup = ('D','H','R','U','V','D','U','T','T')
str = ''.join(tup)
print(str)

#18)program to check whether an element exists within a tuple.

a=(1,3,43,'python','orange',2.1,5.6,'programming')
print('python' in a )
print(50 in a )

#19)program to find the length of a tuple.

a=(10,13,4235,575,744,'python','orange',2.1,5.6,'programming')
print(len(a))

#20)program to convert a list to a tuple.

x = [1,2,50,34,5, 10, 7, 4, 15, 3]
print(x)
#CONVERT IN TUPLE
y = tuple(x)
print(y)

#21)program to reverse a tuple.

x = (1,2,3,50,14,56,78)
y = reversed(x)
print(tuple(y))

#22)program to replace last value of tuples in a list.

x=[(10, 20, 30), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (200,) for t in x])

#23)find the repeated items of a tuple.

x=(1,2,2,3,1,1,2,4,5,6,2,2,4,6,4,4,10)
print(x)

count=x.count(2)
print(count)

#24)remove an empty tuple(s) from a list of tuples.

a = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in a if t]
print(L)


#25)unzip a list of tuples into individual lists.

l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))

#26)convert a list of tuples into a dictionary.

x =  [(1,'Orange'), (2,'Banana'), (3,'Mango'), (4,'Apple'), (5,'Grapes')]
y = dict(x)
print(y)

#27)sort (ascending and descending) a dictionary by value.

x={'Car':3,'Apple':1,'Bike':2,'Dog':4}
l=list(x.items())
l.sort()
print(l)
l.sort(reverse=True)
print(l)

#28)concatenate following dictionaries to create a new one.

a={1:100, 2:200}
b={3:300, 4:400}
c={5:500, 6:600}
dict = {}
for d in (a,b,c): 
  dict.update(d)
print(dict)

#29)check if a given key already exists in a dictionary.

a = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def Check_KeyStatus(x):
  if x in a:
      print('Key is Present In The Dictionary')
  else:
      print('Key is Not Present In The Dictionary')

Check_KeyStatus(5)
Check_KeyStatus(9)  

#30)print a dictionary where the keys are numbers between 1 and 15.

a=dict()
for x in range(1,16):
    a[x]=x**2
print(a)

#31)check multiple keys exists in a dictionary.

sports = {
    '1' : 'Cricket',
    'Vollyball': '2',
    '3' : 'Hockey'
}
print(sports.keys() >= {'3','Cricket'})
print(sports.keys() >= {'Vollyball', '1'})
print(sports.keys() >= { '3' ,'1'})


#32)merge two Python dictionaries

def Merge(a,b):
    return(a.update(b))
a = {1: 10, 2: 20, 3: 30} 
b = {4: 40, 5: 50, 6: 60}
print(Merge(a,b))
print(a)

#33)map two lists into a dictionary.

Keys = [1,2,3]
Values = ['Red', 'Green', 'Blue']
color_dict = dict(zip(Keys,Values))
print(color_dict)

#34)combine two dictionary adding values for common keys.

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)

#35)print all unique values in a dictionary.

L = [{"A":"1"}, {"B": "2"}, {"C": "1"}, {"D": "5"}, {"E":"5"}, {"F":"9"},{"G":"7"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)

#36)create and display all combinations of letters, selecting each letter from a different key in a dictionary.

a={'1': ['a','b'], '2': ['c','d']}
for x in a['1']:
    for y in a['2']:
        print(x + y)

#37)find the highest 3 values in a dictionary.

from heapq import nlargest
dict = {'a':5000, 'b':545, 'c': 560,'d':320, 'e':5874, 'f':6789}  
three_largest = nlargest(3,dict, key=dict.get)
print(three_largest)

#38)combine values in python list of dictionaries.

from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
a = Counter()
for x in item_list:
    a[x['item']] += x['amount']
print(a)

#39)to create a dictionary from a string.

from collections import defaultdict, Counter
str1 = 'w3resource' 
dict = {}
for letter in str1:
    dict[letter] = dict.get(letter, 0) + 1
print(dict)

#40)to calculate the factorial of a number.

n=int(input("Input a number to the factiorial : "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(n))

#41)check whether a number is in a given range.

def number (a,*l):
    if a in range(*l):
        print("Given Number is Available in Range")
    else:
        print("Given Number is Not Available in Range")

number(3,0,10)                                     #3 is available #if 12 then not available

#42)check whether a number is perfect or not.

def perfect(a):
    b=0
    for i in range(1,int(a+1/2)):
        if a%i==0:
            b+=i
    if b==a:
        print(a,"is a perfect number")
    else:
        print(a,"is not a perfect number")
perfect(26)
perfect(28) 

#43)checks whether a passed string is palindrome or not.

def ispalindrome(a):
    start,end=0,len(a)-1
    while start<=end:
        if not a[start]==a[end]:
            return False

            start+=1
            end-=1
        else:
            return True
print(ispalindrome('qwer'))
print(ispalindrome('abcd')) 


#44)read a random line from a file.

import random
file=open("rd.txt",'r')
a=(file.read()).split(".")[:1]
print(random.choice(a)) 

#45)convert degree to radian.

import math
p=int(input("enter value in degree :"))
a=math.pi/p/180
print(a)

#46)calculate the area of a trapezoid.

base_a = 5
base_b = 6
height = float(input("Height of trapezoid: "))
base_a = float(input('Base one value: '))
base_b = float(input('Base two value: '))
area = ((base_a + base_b) / 2) * height
print("Area is:", area)

#47)calculate the area of a parallelogram.

base = float(input('Length of Base: '))
height = float(input('Measurement of Height: '))
area = base * height
print("Area is: ", area)

#48)calculate surface volume and area of a cylinder.

pi=22/7
height = float(input('Height of Cylinder: '))
radian = float(input('Radius of Cylinder: '))
volume = pi * radian * radian * height
sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
print("Volume is: ", volume)
print("Surface Area is: ", sur_area)

#49)returns sum of all divisors of a number.

def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
print(sum_div(8))
print(sum_div(12))

#50)find the maximum and minimum numbers from the specified decimal numbers.

def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))