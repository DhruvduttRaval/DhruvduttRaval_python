l=[1,2,3,1.1,2.2,"tops",10,True,"python",1,2,100,False]

print(l)
print(len(l))
l.append(11)
print(l)
#l.clear()
#print(l)
l1=l.copy()
print(l1)
l1.append(12)
print(l1)
print(l)
l2=l
l.append("jigar")
print(l2)
print(l)
a=["Vinit","Mayank",1.1,200,True]
l.extend(a)
print(l)
print(l.count(1))
print(l.index(10))
l.insert(5,50)
print(l)
l.pop()
print(l)
l.pop(10)
print(l)
l.remove(10)
print(l)
l.reverse()
print(l)
#l.sort()

for i in l:
    print(i)

s="Tops Technologies"
for i in s:
    print(i,end="*")

for i in range(1,10):
    print(i*"*")
