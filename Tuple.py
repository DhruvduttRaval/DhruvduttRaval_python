#Collection of data can't change with runtime. () - Round bracket used in tuple.

t = (1,2,10,1.1,"Tops",True,"Python",1,2,100)
print(t)
print(t.count(1))
print(t.index(100))

for i in t:
    print(i)

print(1.1 in t)
print(t[5])
t[5].append(40)
print(t[5])
t.append(1000)