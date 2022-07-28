#magic method:- (__init__) - double underscore is called magicmethod
#str method :- firstly object are print then after str method run.
#Return argument always in {} - curley bracket.

#************************************************************
#1)

''' class Point:
    def __init__(self,x,y):
        print("init Called")
        self.x=x
        self.y=y
        print("x : ",self.x,"y :",self.y)

    def __str__(self):
        print("str Called")
        return("{0},{1}".format(self.x,self.y))

P1 = Point(10,20)
print(P1) '''

#************************************************************
#2)  addition :-

''' class Point:
    def __init__(self,x,y):
        print("init called")
        self.x=x
        self.y=y
        print("X :",self.x,"Y: ",self.y)
    def __str__(self):
        print("str called") 
        return "{0},{1}".format(self.x,self.y)
    def __add__ (self,obj):
        print("add called")
        x=self.x+obj.x
        y=self.y+obj.y
        return Point(x,y)
        
p1=Point(10,20)
p2=Point(30,40)
print(p1)
print(p2)
print("Addition :",p1+p2) '''
