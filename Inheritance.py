#Types Of Inheritance :- 1) Single 2)Multilevel 3)Multiple 4)Hierarchical 5)Hybrid


#1) Single inheritance.

''' class A :
    def getA (self,a):
        self.a=a
    def putA(self):
        print("A :",self.a)

class B(A):
    def getB (self,b):
        self.b=b
    def putB (self):
        print("B :",self.b)

b1 = B()
b1.getA(10)
b1.getB(20)
b1.putA()
b1.putB()  '''


#2) Multilevel inheritance.

''' class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A :",self.a)
        
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B :",self.b)

class C(B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C :",self.c)

b1=C()
b1.getA(10)
b1.getB(20)
b1.getC(30)
b1.putA()
b1.putB()
b1.putC()  '''
 
#3) Multiple inheritance.

''' class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A :",self.a)
        
class B:
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B :",self.b)

class C(A,B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C :",self.c)

b1=C()
b1.getA(10)
b1.getB(20)
b1.getC(30)
b1.putA()
b1.putB()
b1.putC()   ''' 

#4) Hierarchi inheritance.

''' class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A :",self.a)

class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B :",self.b)

class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C :",self.c)

class D(A):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D :",self.d)

b1=B()
c1=C()
d1=D()

c1.getA(10)
b1.getB(20)
c1.getC(30)
d1.getD(40)

c1.putA()
b1.putB()
c1.putC()
d1.putD()  '''

#5) Hybrid inheritance.

''' class A:

    def getA(self,a):
        self.a=a
    def putA(self):
        print("A : ",self.a)

class B(A):

    def getB(self,b):
        self.b=b
    def putB(self):
        print("B : ",self.b)

class C(A):

    def getC(self,c):
        self.c=c
    def putC(self):
        print("C : ",self.c)

class D(B,C):

    def getD(self,d):
        self.d=d
    def putD(self):
        print("D : ",self.d)

d1=D()

d1.getA(10)
d1.getB(20)
d1.getC(30)
d1.getD(40)

d1.putA()
d1.putB()
d1.putC()
d1.putD() '''