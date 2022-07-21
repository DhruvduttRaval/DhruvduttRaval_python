# to write or read file or append another file
# file handling available in c/c++ and java
# write ma file location par nai hoy to navi create kari dese
# read and append ma file location par hovi jaruri 6
# txt format every OS par available 6.. mac,windows, ubuntu, linux that's why we use txt

#1.) write 2.)read 3.)append

file=open("tops1.txt","w")  # or c:\\tops1.txt
file.write('This is file management demo using python')
file.close()
print("file written successfully")


file=open("tops1.txt","r")
print(file.read())
file.close()


file=open("tops1.txt","a")
file.write("\nnow this file is appended")
file.close()
print("file appended successfully")
file=open("tops1.txt","r")
print(file.read())
file.close()



# in file we can only insert string value.

#(*) w+ = Write and Read

file=open("tops2.txt","w+")
file.write("this is w+ operation in file management using python")
print("cursor position :",file.tell())

file.seek(0)
print(file.read())
file.close()

#(*) r+ = Read and Write            #file existing imp.

file=open("tops2.txt","r+")
file.write("this is r+ operation in file management using python")
print(file.read())
print("file r+ successfully")
file.close()


#********************Programme:-1********************

import random 
#print(random.randint(1,10))
file = open("data.txt","w")
for i in range (10):
    num = random.randint(1,10)
    file.write(str(num)+",")
file.close()

file = open("data.txt","r")
print(file.read())
file.close()

file = open("data.txt","r")
l=file.read().split(",")[:-1]
for i in l :
    print(i)
file.close()
print(l)

#********************Programme:-2********************
file = open('data.txt','r')
odd = open('odd.txt','w')
even = open('even.txt','w')
prime = open('prime.txt','w')

l = file.read().split(',')[:-1]
for i in l:
    if int(i)%2==0:
        even.write(i+',')
    else:
        odd.write(i+',')
    if int(i)%2!=0:
        for j in range (3,int(int(i)/2)+1,2):
            if int(i)%j==0:
                break
        else :
            prime.write(i+",")              

even.close()
odd.close()
file.close()
prime.close()

print('Data File Content')
data = open('data.txt','r')
print(data.read())
data.close()


print('Even File Content')
even = open('even.txt','r')
print(even.read())
even.close()

print('Odd File Content')
odd = open('odd.txt','r')
print(odd.read())
odd.close()

print('Prime File Content')
prime = open('prime.txt','r')
print(prime.read())
prime.close()


