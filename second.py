#This file contains all the contents of chapter 2
#Expressions
#The meaningful names given to variables so that the user can understand..
#the code better, i.e. for human.
print(2**10)  # power calculation

#Numerical evaluations
#Order of evaluation...Operator preferences
#parantesis > power > multiplication > addition > left to right
print(1 + 2 ** 3 / 4 * 5)

x=1+4                   #This is interger addition
print(x)
p="Mohit "+"Rohilla"    #This is string concatenation
print(p)                #Will not be added chill

#q="Mohit "+1           Type error
#print(q)               this becomes bull shit...

type("x")
type('hello')
type(1)

print(float(1)+2)   #Store the value of 1 to 1.0
print(9/2)          #python 3 automatically does the conversion to float

c='123'
#print(c+1)          #this is an error
type(c)             #here c is a str now
c1=int(c)           #now c1 becomes an interger
print(c1+1)         #since c had all int so it was possible

d='mohit'
#d1=int(d)          #this is not permitted my dear

name=input("who are you:")          #Inout from the user, this is always str
print("Welcome", name)              #one space inserted by this comma also

print(9/3)                  #this stores the value as 3.0 i.e. "/" --> float

Rate=input("Give the rate value:")   #This input value of rate is saved as a string...
                                    #So, to use this in the maths calculations first convert to int/float
