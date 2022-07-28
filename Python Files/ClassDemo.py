class student:

    def getdata(self,fname,lname):
        print("getdata called")
        self.f=fname
        self.l=lname
    
    def putdata(self):
        print("putdata called")
        print("First Name : ",self.f)
        print("Last Name : ",self.l)
    
s1=student()
s2=student()

s1.getdata("Dhruvdutt","Raval")
s1.putdata()
s2.getdata("Tops","Technology")
s2.putdata()
