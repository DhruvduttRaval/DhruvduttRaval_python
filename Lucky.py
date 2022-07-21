import random

a = [10,20,'Tops',1.1,True,'Python',False,1]
lucky = []
for i in range(1,101):
    a.append(i)
for i in range (10):
    num = random.choice(a)
    lucky.append(num)
    a.remove(num)

print(a)
print(lucky)