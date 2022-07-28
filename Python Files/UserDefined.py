#two types of functions :- 1) Userdefined Function 2) Library Function
#Fun :- Function is a set of instruction that perform a specific task.

#1) Function With No Argument & No Return Value.

#def :- for define function
#() - Parameter
#(ioacaco) - print something is called argument.


def printLine ():
    print("*" * 50)
printLine ()
print("Welcome To User Defined Function To Python")
printLine()

#2) Function With Argument But No Return Value.

def add(a,b):
    print("Addition :",a+b)
add(10,20)

#***************Dynamic Method:-
def add(a,b):
    print("Addition :",a+b)
x = int(input("Enter Value :"))
y = int(input("Enter Value :"))
add(x,y)

#3) Function With Argument And Return Value.
#1.Method:1 // Only Dynamic:-
def sub(a,b):
    return a-b
printLine()
x = int(input("Enter Value :"))
y = int(input("Enter Value :"))
print(sub(x,y))

#2.Method:2 // Dynamic With Using Variable:-
def sub(a,b):
    return a-b
printLine()
x = int(input("Enter Value :"))
y = int(input("Enter Value :"))
z = sub(x,y)
print("Subtraction :",z)


























