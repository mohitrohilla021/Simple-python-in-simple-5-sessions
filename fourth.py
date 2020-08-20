# Functions
# Reusable piece of code
# Function acts like a variable that holds the complete code
def new_function():                 # Now, python doesn't executes it, it remembers it and executes if further when required
    print("You called the function...")
    print("function is being executed")

new_function()              #This the the function call
# After executing the function when its called the control again comes to the same point
print("Hello this is main program")
new_function()

# max Function & min Function
# These functions are predefined in the language itself

bigger=max("hello world")
print(bigger)
smaller=min("Hello world")       # " " space is considered as the smallest
print(smaller)

compare=max("wW")                # w is considered bigger than W
print(compare)

# def function only defines(stores) a function, never executes it
# the function need to be "called" or "invoked"

# Function with the parameters

def comment_on_cgpa(cgpa):
    try:
        cgpa_float=float(cgpa)
    except:
        cgpa_float=-1               # in case, invalid input has been entered by the user
    if cgpa_float<0:
        print("Invalid input...")
    elif cgpa_float<6.0:
        print("Soory, you didn't qualify...")
    elif cgpa_float<9.0:
        print("Great, you have passed...")
    elif cgpa_float<10.0:
        print("Waw, you got a great score, you are among scholars")
    else:
        print("Invalid input")

marks=input("Enter your cgpa:")
comment_on_cgpa(marks)

# function return statement

def hello_world():              # just to demonstrate the return statement use
    return "hello world"        # this becomes the residual value
# hello_world()                 # only this doesn't actually prints that retuen statement
print(hello_world())            # this is the function invoke, need to be with "print" statement

# function to add two numbers
print("Lets add two numbers:")
x=input("Enter first number:")
y=input("Enter second number:")
def addition(x,y):
    try:
        x_float=float(x)
        y_float=float(y)
    except:
        x_float=-1
        y_float=-1
    if x_float==-1:
        return -1
    elif y_float==-1:
        return -1
    else:
        return x_float+y_float
sum=addition(x,y)
if sum==-1:                 # if the sum is really -1 then also it will show invalid input
    print("Invalid input")  # say 99-100 will show invalid input...
else:
    print("The sum is:",sum)

# to solve this problem...

print("Lets add two numbers:")
x=input("Enter first number:")
y=input("Enter second number:")
def addition(x,y):
    try:
        x_float=float(x)
        y_float=float(y)
    except:
        x_float=-1
        y_float=-1
    if x_float==-1:
        return "invalid input"      # this time there is no -1 returned
    elif y_float==-1:
        return "invalid input"      # this time there is no -1 returned
    else:
        return x_float+y_float
sum=addition(x,y)
print(sum)

# an int type and a float type cannot value cannot be directly multiplied
