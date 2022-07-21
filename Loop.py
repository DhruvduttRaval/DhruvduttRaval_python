# '''for i in range (1,10):
#     for j in range (i):
#         print ("*",end="")
#         print()'''

# #***********************************************************
# #Ex :1 
# for i in range (1,10):         #for making * pattern
#     print ("*" * i)

# #***********************************************************
# #Ex :2
# for i in range (1,10):         #mirror * design
#     print (" " *(9-i),"*"*i)

# #***********************************************************
# #Ex :3
# for i in range (1,10):         #triangle * design
#     print (" " *(9-i)," *"*i)

# #*********************************************************** 
# #Ex :4
# for i in range (1,10):
#     print (" "*(9-1),"*"*i)
# for i in range (9,0,-1):
#     print (" "*(9-1)," *"*i)

# #*********************************************************** 
# #Ex :5
# for i in range (1,10):
#     print (""*(9-1),str(i))

# for i in range(1,10):                  #1 to 123456789 pattern
#     for j in range(1,i+1):
#         print(j, end='')
#     print()
 
# for i in range (1,10):
#     print (" "*(9-1)*i,"*"*i)
# for i in range (9,0,-1):
#     print (" "*(9-1)," *"*i)

# for i in range(9,0,-1):                   #9 to 987654321 pattern
#     print (""*i,*range(9,i-1,-1))


#*********************************************************** 

# n = int(input("ENTER N :"))            #Fibonacci series - while loop
# sum = 0

# while n>0:
#         sum=sum+n
#         n -= 1
# print("SUM :",sum)

#***********************************************************

# n = int(input("ENTER N :"))            #Fibonacci series - for loop
# sum = 0

# for i in range(1,n+1):
#     sum=sum+i
# print("SUM :",sum)


