# Conditional statements
# Here, is where the coders intelligence plays an important role
# take care, "=" is the assignment & "==" is a question

# There is difference between spaces and tab
# python things this to be different
# as a file is saved by .py extn the atom automatically converts the tab into spaces
# Other editors enable "auto-epanded tabs"

# Indentation plays a very crutial role Here

marks=input("Enter your marks:")     # input function always stores in str format
marks_int=int(marks)
if  marks_int>=30:
    print("You are passed.")
    marks_int=int(marks)                 # the marks for comparision needed in int
else:
    print("Opps... You are failed.")

# for loop

for i in range (5):         #Takes the values from 0 to n-1
    print(i)
    if i>=1:                #This if is nested
        print("The number is not 'null'")
    print("Done with i ", i)
print("all done")

#To demonstarte the use of elif & try-except block

var=input("Enter your CGPA:")
#var_float=float(var)              #Value error arises if the user puts something except float in  var
                                #So, to solve this problem, we use try block
try:
    var_float=float(var)   #If this line blows up, then the lines below it(in try block) will be skipped
except:
    var_float=-1          #if this above try code blows up then the python runs this except block
if var_float<0:
    print("The value entered is invalid...")
elif var_float<5:
     print("Very poor performance")
elif var_float<7:
     print("need improvement")
elif var_float<9:
    print("The performance is okay...lets see your skillset.")
elif var_float<10:
    print("Awesome, great performance, lets see your skillset.")

#The try-except blocks helps a lot in case of user entering wrong values

# try- except demonstartion 2

marks=input("Enter your marks:")     # marks is stored in str format
try:
    marks_int=int(marks)
except:
    marks_int=-1
    # print("Wrong value entered...")
    # quit()                                # This can be used to eliminate the irritating "traceback message"...
                                            # that occurs if the value input by the user is wrong.
if marks_int>0:
    if  marks_int>=30:
        print("You are passed.")    #the marks for comparision needed in int
    else:
        print("Opps... You are failed.")
else:
    print("The entered value is invalid...")
