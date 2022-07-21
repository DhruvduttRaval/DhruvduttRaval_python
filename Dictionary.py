# {} - Dictionary Bracket
# 1. Pairing elements - keyend value.
# Key Must Be Unique. Value Can Be Anything.
# Our Data Access By Key.
# its Called Key - 1 : Dhuruvdutt - its Called Value (Pair Of Key & Value is Called Dictionary)

# Difference Between POP List & POP Dictionary.

#POP list                            POP Dict
#1.Only Last Element Removed        1.Argument Compulsory For Remove Any Element. 
#  (Without Argument)

#2.pop() - last element             2.popitem()-write argument in bracket.


#Ex : 1
''' d={1:'Dhruvdutt'}
for i in d:
    print(i)                 #only print key
    print(i, ":", d[i])      #key and value both are print   '''


''' d={1:"Vinit",2:"Amit",3:"Savan",4:"Dhruvdutt",5:"Naresh",6:"Sonalisha",7:"Mayank",8:"Krupa",9:"Ronak"}

print(d)
print(d[3])
#print(d["Amit"])
d1=d.copy()
print(d1)
print(d.get(5))
print(d.items())
print(list(d.keys()))
print(d.values())
print(d.pop(3))
print(d)
print(d.popitem())
print(d)
d2={10:"Mehul",11:"Harsh",12:"Ravi",13:"Rehan"}
d.update(d2)
print(d)

for i in d:
    print(i," : ",d[i])  ''' 


#Ex :- 2 (Square Of Values)
n=int(input("Enter N:"))
d={}

for i in range(1,n+1):
    d[i]=i*i

print(d)
  