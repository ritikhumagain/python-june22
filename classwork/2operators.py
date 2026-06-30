# arithmetic operator
# Arithmetic operators are used to perform mathematical calculations like addition,sub etc
# +	Addition	             5 + 3 → 8
# -	Subtraction	             5 - 3 → 2
# *	Multiplication	         5 * 3 → 15
# /	Division	             5 / 2 → 2.5
# //	Floor Division	     5 // 2 → 2
# %	Modulus (Remainder)	     5 % 2 → 1
# **	Exponent (Power)     5 ** 2 → 25

add = 1 + 2  # Here + is operator and 1 and 2 are operant
print(add)
sub = 2 - 1
print(sub)
multi_no = 2 * 2
print(multi_no)
div_no = 4 / 2
print(div_no)  # Ans will come in float
floor_divisin = 5 // 2
print(floor_divisin)
remainder_no = 3 % 2  # same as division but gives lowest whole no
print(remainder_no)
exponent_no = 2**2
print(exponent_no)  # used for power function

# we can we perform arithmetic operation in string
# addition in string
first_name = "Ram"
last_name = " Adhikari "
full_name = first_name + last_name
print(full_name)  # this is know as concatenation
print(type(full_name))
first_name1 = 10  # integer
last_name1 = "Adhikari"  # sting
# print(first_name1+last_name1)
# print(full_name) # error will occur
print("1" + "1")  # pydantic is used to resolve this problem

# Multiplication on string
# Here one should be string and one should be integer or error may occur
print("a" * 5)


# comparision operator
# Comparison operators are used to compare two values.
    # ==	Equal to	5 == 5	True # also used for string
    # !=	Not equal to	5 != 3	True # Also used for string
    # >	Greater than	5 > 3	True # from here it is not used in string
    # <	Less than	5 < 3	False
    # >=	Greater than or equal to	5 >= 5	True
    # <=	Less than or equal to	5 <= 3	False
a = 4 
b = 4 
c = "4"
print(a == b)
print(a == c) # Equal to 
print(a != c) # Not equal to 
print(5>3) # Greater than 
print(5<19) # less than 
print(5>=5) # greater or equal to 
print(5<=5) # lessthan or equal to
print(2!= 1) # Not equal to 
print("hari"=="hari") # we can use string too 


#Logical operator 
# Logical operators are used to combine two or more conditions.
    # and	Both conditions must be True
    # or	At least one condition must be True
    # not	Reverses True to False and False to True
result_show = True
print(not(result_show))  # not
print( 1 == 1 and 5> 3 ) # and 
print( 1 == 1 or 5> 13 ) #or 
# using and 
age = 20 
citizen = True
print(age>=18 and citizen)  # value must be true 
# Using or 
is_weekend = False
is_holiday = True
print(is_weekend or is_holiday) # value must be true
# Using not 
logged_in = False
print(not logged_in)


#Assignment operators 
# Assignment operators are used to assign or update values in variables.
    # =	    x = 5	Assign 5 to x
    # +=	x += 3	x = x + 3
    # -=	x -= 3	x = x - 3
    # *=	x *= 3	x = x * 3
    # /=	x /= 3	x = x / 3
    # //=	x //= 3	x = x // 3
    # %=	x %= 3	x = x % 3
a = 5 
b = 5
b += a # b = b+ a 
print(b)



# 🧪 Practice Questions
# Arithmetic Operators

# Write a program that asks the user for two numbers and prints the result of all 7 arithmetic operations on them.
# A shopkeeper has 100 apples. He sells them equally to 6 customers. Print how many each customer gets (floor division) and how many are left over (modulus).
# Ask the user for the base and exponent, then print the power result using **.

# String Arithmetic

# Ask the user for their first and last name separately, then join them using + and print the full name.
# Ask the user for a word and a number, then repeat that word that many times using *.

# Comparison Operators

# Ask the user to enter two numbers. Compare them using all 6 comparison operators and print each result.
# Ask the user to enter two words and check if they are equal using == and not equal using !=.

# Logical Operators

# Ask the user their age and whether they have a valid ID (True/False). Print whether they are allowed entry if age must be 18+ and they have an ID.
# A user can get a discount if they are a student or a senior citizen. Ask both questions and print if they get a discount.

# Assignment Operators

# Start with a variable score = 0. Then:

# Add 10 using +=
# Multiply by 2 using *=
# Subtract 5 using -=
# Print the final score after each step




# 💼 Interview Questions
# Arithmetic

# What is the difference between / and // in Python?
# What does the % operator do? Give a real use case (Hint: checking even/odd)
# What happens when you divide by zero in Python?

# String Operations

# Can you add a string and an integer directly in Python? Why or why not?
# What is string concatenation and how is it different from f-strings?

# Comparison

# What is the difference between = and == in Python?
# If a = 4 and c = "4", why does a == c return False?

# Logical

# What is short-circuit evaluation in and / or?

# In and — if the first condition is False, Python skips the second
# In or — if the first condition is True, Python skips the second


# What does not return if the value is 0? What about None?

# Assignment

# What does x += 3 actually mean internally?
# What is the difference between x = x + 1 and x += 1? Are they always the same?


# 🏆 Mini Challenge
# Build a simple grade calculator:

# Ask the user for marks in 3 subjects
# Calculate the total using +=
# Calculate the average using /
# Print whether the student passed using a comparison (>=40) combined with and for all three subjects