# Loops and iterations
# Repeating steps
# "while" and "for" Loops
# while for "indefinite" Loops and for is for "definite" Loops

# while
n=1
while n<5:                          # this condition statement is checked agian and again, every time this block terminates
    print("Loop exection time ",n)
    n=n+1
print("termination reached, last execution:",n-1)

# the biggest problem in loops is when it enters a "infinite" loops, so take care of that...

# break statement can be used in the loop
while 1:
    choice=input("Enter something:")
    if choice=='done':
        break
    print("Invalid input... try 'done'")
print("Yes, this is accepted")

# This break can be best used when presenting a menu to the user to select any option from the given ones...

while 1:                # 1 can also be replaced by True.
    choice_new=input("Which operation do you want to perform:\n1.View\n2.Edit\n3.Delete\n4.Exit\nEnter your choice:")
    if choice_new=='4':
        break                   #This if executed the loop gets terminated
    print("This is unavailable right now...")
print("great, program terminated...")


#   Continue is used to skip that perticular iteration only
#   Generally used when a finite amount of iterations are needed

# Program to check if the input line is a comment

while True:
   line_input=input("Enter some line:")
   if line_input[0]=='#':
       continue                                     #Takes the execution again to next condition
   else:
     print("This line is not accepted as a comment...")
     break
print("done...")

# For loop
# these are definite loops
# The iteration value iterates through sequence(ordered set)
# [] denotes the "list" of items

for i in [5,4,3,2,1]:               # [] and () both can be used, even without braces this works fine
    print(i)                        # there is no need of increment of i here...
print("Loop finished")

# the example of  list in python

list_1=[1,2,3]
lsit_2=['mohit','rohit','mohan','sohan']

#Program to print the largest no. of the given list

largest_so_far = -1
print("before",largest_so_far)
for num in [1,2,45,21,23,65,32,21,78,3,64,11]:
    if num > largest_so_far:
        largest_so_far=num
    print(num,largest_so_far)
print("After completion of the loop largest found is:",largest_so_far)

# loop idioms

#summing all the values in a loop
total_sum=0
for num in [1,2,45,21,23,65,32,21,78,3,64,11]:
    total_sum =total_sum + num
    print(num,"added:",total_sum)
print("Final total of the amount is:",total_sum)

# filtering can also be used inside the loop using if statements

# Boolean variable
# lets find a number in the list

found=False
found_status=False
print("before",False)
for num in [1,2,45,21,23,65,32,21,78,3,64,11]:
    found=False
    if num==65:                 # assumed that the no. to search is 65
        found=True
        print(num,found)
        found_status=True       # this is to record the final data is found or not
        continue
    print(num,found)
print("After",found_status)

#Program to print the smallest no. of the given list

# smallest_so_far = -1                # this initialisation creates problem in the output here
# so, we have a "None" type,
# none denotes the "no number"

smallest = None                 # this is flag value
print("before",smallest)
for num in [1,2,45,21,23,65,32,21,78,3,64,11]:
    if smallest is None:
        smallest=num            # the program assumes the first one to be smallest
    elif num<smallest:
        smallest=value
    print(smallest,num)
print("After completion of the loop smallest found is:",smallest)

# "is" and "is not" are the logical operators in python language
# "is" is similar to "==", but is even more stronger than it.
