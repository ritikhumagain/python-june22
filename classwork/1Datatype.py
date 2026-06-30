# is used to comment the line which dont need in a code or which may occur error in the functional code
# we
# can
# use
# clt slas
# to comment
# multiple
# line


# creating variable
# rule python follow indentation
a = 10  # integer - number
ab = "hello"  # string - word
a = 111  # feari hami le teslai realocate garna sakcham
A = 1  # python is casesensitive
aa = 1

# how can we make variable
data = 44
data_test = "testing "  # we can use underscore
firstName = "ritik"  # we can use upercase or lower case
test1 = "testing "  # we can use number
last_name = "humagain"  # we can use only one underscore
lastname_ = "hello"


# what cannot we do
# 1test = 1000    # we cannot use number
# we cannot use reserve word for eg print
# we cannot use other symbol for eg #@! etc except underscore


# how to run this code
# first you have to save the file - you can make auto save from file
# open terminal  - shortcut clt shift backtick
# and type python and file name
# and to clear you can type cls

# console ma keahi print vako chaina
# so we have print() function to print into the console
first_name = "ritik"
last_name = "humagain"
print(firstName)
print(last_name, 1, 2, 3, 4, 5, "helloworld")  # comma vayo vane space aaucha


# creating virtualenv
# virtualenv is tool used in python development to create isolated python environment
# how to create
# first go to terminal and type python -m venv and environment name it is ususally written as env vnv etc
# Now how to activate the environment
# environmentname\Script\activate # window user
# mac and linus source environmentname/bin/activate


# guidlines
# to write python code there are some guidelines we have to follow
# for example there should be space infornt and in last of an operator
# there should be space after the comma
# So we have one package that tell you where guideline are voiloted
# so we have to activate flake8
# we can install flake8 - pip install flake8
# there is blackformating extension to resolve this problem


# Data type
# common data types
# - string ("") : Text enclosed in quotes . eg "hello ", 'world'
# - Interger (11)
# Float(2.0)
# Complex( ): Numbers with real and imaginary part. Eg (2+3j )
# Boolean (): Represent Ture or False
# None () : Represent the absence of a value

student_name = "john"  # String
class_studied = 7  # interger
student_height = 5.11  # Float
self_manner = True  # Boolean
hoobies = None  # None
equation = 2 + 5j  # Complex
# how to check its data type
# we have one function called type() function
print(type(equation))
# print(type(student_height,student_name, class_studied, self_manner, hoobies)) # it will accept only one argument


# To take input from user we have input function
print("enter your age ")
age = input("student enter your age:")  # inside quote will display your msg
print("your age is ", age)
print(type(age))

# Type casting
# the process of changing one data type into another data type is know as type casting
name_emp = "ram"  # here we cannot change it to interger
s_no = 10  # here we can change it to string
age_employee = int(input("sir enter your age :  "))
print(type(age_employee))

# Type valuation
name = "Ram "
print(isinstance(a, int))

# String formating
first_name = "Ritik"
last_name = "Humagain"
address_is = "Balaju"
print("my name is : ", first_name)  # when we have to use only one
# fsting function is used for multiple input in print
print(
    f"My name is {first_name} {last_name}. I lived in {address_is}"
)  # It can be readable to so

# HomeWork
# Level 1 — Variables & Data Types
# Create variables to store your own name, age, height, and whether you are a student (True/False). Print all of them.
#  Create a variable for each data type (string, integer, float, boolean, None, complex) and use type() to print the type of each one.


# Level 2 — Input & Type Casting
# Ask the user to enter two numbers using input(), add them together, and print the result. (Hint: you'll need int() or float() casting)
# Ask the user for their first name and last name separately, then print a greeting using an f-string.


# Level 3 — String Formatting & isinstance()
# Create 3 variables — a name, a city, and an age — then print a full sentence using an f-string like:
# "Hi, I am Alex, I am 20 years old and I live in Pokhara."
# Create any variable and use isinstance() to check if it is a string, then check if it is an integer. Print both results.


# Level 4 — Mini Challenge
# Build a simple user profile program:
# Ask the user for: name, age, city
# Cast age to integer
# Print a formatted profile card using f-strings
# Use type() to confirm that age is stored as an integer


# Naming Rules Bonus
# Write 5 valid variable names and 3 invalid ones (as comments explaining why they are invalid) — based on the rules you noted in your code.
