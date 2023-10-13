print("Hello, world")

#decalre varible by assigning a value. and without assign a value variable cant decalre.
x="5"
y="hello"
print(x)
print(y)

#change varibale type
x="hello"
print(x)

#casting - give specify a variable to their data type
x = int(3)
a = str("Mihir")
y = float(3)
print(x,"int",y,"float",a,"str",)

#get data type with type() funaction 
print(type(x))
print(type(a))
print(type(y))

#multiple varibale in one line

a, b, c = "mihir", "5", "4.0"
print(a,b,c)

#one value to multiple variable but focus on syntax a=b=c= "reet"

a= b= c= "reet"

print(a,b,c)

#unpack list - if you have collection of value in list,tuple etc. pythone allows to extracs values in variable.
#this called unpacking

fruits =["banana","orange", "mango"]
print(fruits)

#unpacking in variables
x,y,z= fruits 
print("x",x,"y",y,"z",z)

#print() function used as a output variable
#you can + operator to output multiple variable

print(x+y+z)

#notice space character

x="python "
y="is "
z="awesome"
print(x,y,z)
print(x+y+z)

#spaces remove in varibales using + operator
x="python"
y="is"
z="awesome"
print(x,y,z)
print(x+y+z)

#+ character work as matchmatics operator
x=3
y=5
print(x+y)

#global variable - you can used outside and inside function

x="reet"

def myfun():
    x="mihir"
    print("he is " + x)

myfun()
print("this is " + x)

#create global variable inside function

def myfunc():
    global t 
    t= "mihir"
myfunc()
print("he is "+t)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

o = "reet"

def myfun1():
        global o
        o="dhwani"
        print("yes..she is "+o) #this called indentation..this line is inside function that's why output is dhwani 
print("yes..she is "+o) #outside the function this line because output is reet
myfun1()    
print("she is "+o)

#DataTypes in python

#Text Types - str
a="mihir"
print("this is str data type =",a)

#Numeric Types - int, float, complex
b=5
print("this is int data type =",b)

c=2.0
print("this is float data type =",a)

d=1j
print("this is complex data type =",a)

#Sequence Types - list, tuple, range list is mutuable, tuple is immutable means list can be modified and tuple cant be modified
e=["mihr","hitesh","krinal"]
print("this is list data type =",a)

f=("mihir","hitesh","krinal")
print("this is tuple data type =",a)

#Syntax: range(start, stop, step)
'''Python’s range() method returns a sequence of numbers starting from start to stop, with step'''
'''start: [ optional ] start value of the sequence
stop: next value after the end value of the sequence
step: [ optional ] integer value, denoting the difference between any two numbers in the sequence
Return : Returns an object that represents a sequence of numbers'''
g=range(6)
print("this is range data type =",a)

#Mapping Type - dict
h={"name":"mihir","age":25}
print("This is Dict data type =",h)

#Set Types - set, frozenset.differance - set ismutubale object tht can allow to chnage in objcet.and frozen set is amutbale object that cant allow you to change in objcet.

i={"apple","banana","cherry"}
print("this is set data type ",i)

j=({"apple","orange","banana"})
print("this is frozenset data type ",j)

#Boolean  Type - bool
k= bool(10)
print(k)

'''Here are a few cases, in which Python’s bool() method returns false. Except these all other values return True. 

If a False value is passed.
If None is passed.
If an empty sequence is passed, such as (), [], ”, etc.
If Zero is passed in any numeric type, such as 0, 0.0, etc.
If an empty mapping is passed, such as {}.
If Objects of Classes having __bool__() or __len()__ method, returning 0 or False.'''

# Returns False as x is False
x = False
print(bool(x))
 
# Returns True as x is True
x = True
print(bool(x))
 
# Returns False as x is not equal to y
x = 5
y = 10
print(bool(x == y))
 
# Returns False as x is None
x = None
print(bool(x))
 
# Returns False as x is an empty sequence
x = ()
print(bool(x))
 
# Returns False as x is an empty mapping
x = {}
print(bool(x))
 
# Returns False as x is 0
x = 0.0
print(bool(x))
 
# Returns True as x is a non empty string
x = 'GeeksforGeeks'
print(bool(x))

#Binary Types - bytes, bytearray, memoryview

x= b"mihir"
print("this is bytes data type =",x)

y= bytearray(4)
print("this is bytearray data type =",y)

z= memoryview(bytes(6))
print("this is memoryview data type =",z)

# None Type - NoneType
x=None
print("this is NoneType data type =",x)

#type conversion

x=1
print("this is int data type =",x,type(x))

y=(float(x))
print("this is flaot data type =",y,type(y))

z='1'
print('this is string',z)

a=(int(z)+1) #i converted z in to intezer and then plus 1, without using int i cant be converted str into int
print('add value in z',a)

#random nuber generator random module have its own set of methods only 

import random
print(  random.randrange(20,90))

