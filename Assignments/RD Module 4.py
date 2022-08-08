#************MODULE :-4*****************RD-File.py

#1)to read an entire text file.

f=open("RD.txt","r")
print(f.read())
print(f.close())

#2)to append text to a file and display the text.

f=open("RD.txt","a")
f.write("U have added sentence in previous file")
f.close()

#3)to read first n lines of a file.

n=int(input("Enter Start Line Number :"))
f=open("RD.txt","r")
r=(f.read())
f.close()
a=(r.split("\n"))
for i in a[:n]:
    print(i)

#4)to read Last n lines of a file.

n=int(input("Enter Last Line Number :"))
f=open("RD.txt","r")
r=(f.read())
f.close()
a=(r.split("\n"))
for i in a[-n:]:
    print(i)

#5)to read a file line by line and store it into a list.

f=open("RD.txt","r")
r=(f.read())
f.close()
a=(r.split("\n"))
print(a)

#6)to read a file line by line store it into a variable.

f=open("RD.txt","r")
r=(f.read())
f.close()
a=(r.split("\n"))
o=""
for i in a:
    o=o+1
print(o)

#7)to find the longest words.

def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('RD.txt'))


#8)to count the number of lines in a text file.

f = open("RD.txt","r")
a = f.read()
count =0

for i in a:
    if i == "\n":
        count+=1
print(count)

#9)to count the frequency of words in a file.

from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("RD.txt"))

#10)to write a list to a file.

f = open("RD.txt","w")
l1 =[1,2,3,4,5]
for i in l1:
    f.write(str(i))

#11)to copy the contents of a file to another file.

from shutil import copyfile
copyfile('rd.py', 'abc.py')

#12)user to enter only odd numbers, else will raise an exception.

#13)class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle :
    def __init__(self,h,b):
        self.h = h
        self.b = b
        a = self.b * self.h / 2
        print("area =",a)

r1 = Rectangle(10,10)

#14)class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

c1 = Circle(8)
print(c1.area())
print(c1.perimeter())

#15)How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

try:
    a=5
    print(a)
except:
    print("except executed")
finally:
    print("finally executed")

















