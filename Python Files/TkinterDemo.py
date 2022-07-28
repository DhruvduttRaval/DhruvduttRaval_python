from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("My Tkinter Example")

l_id=Label(root,text='ID')
l_id.place(x=50,y=50)

l_frame=Label(root,text="FIRST NAME")
l_frame.place(x=50,y=100)

l_frame=Label(root,text="LAST NAME")
l_frame.place(x=50,y=150)

l_email=Label(root,text="EMAIL")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE")
l_mobile.place(x=50,y=250)

root.mainloop()