#Conditional statements help you execute certain blocks of code only when specific condition are true.

#If  else statement - 
# if(condition):
# statement

# The if statement is used to make decisions in a program.
# It checks a condition:
    # If the condition is True, the code inside the if block runs.
    # If the condition is False, the code inside the if block is skipped.
age= int(input("enter your age"))
if (age>=18): # intendation
    print("You can vote ") # 
if(age<=18): 
    print("you cannot vote ")

cp= 1000
sp = 12

percentage_obtained = int(input("enter your percentage"))
if(percentage_obtained>=90 and percentage_obtained<=100):
    print("you have obtained dictincion")
if(percentage_obtained>=80 and percentage_obtained<90):
    print("you have obtained first division ")
if(percentage_obtained>=70 and percentage_obtained<80):
    print("you have obtained second division ")
    # you can check this from debug section 


# if else 
# The if-else statement lets a program choose between two options.
    # If the condition is True → run the if block.
    # If the condition is False → run the else block
age= int(input("enter your age"))
if (age>=18):
    print("You can vote ")
else:    #here we dont have to write condition 
    print("you cannot vote ")


# elif 
if(percentage_obtained>=90 ):
    print("you have obtained dictincion")
elif(percentage_obtained>=80 ):
    print("you have obtained first division ")
elif(percentage_obtained>=70 ):
    print("you have obtained second division ")
else:
    print("fail")

print("-----"*10)


# nested if :You use nested if else when you want to make another decision only after the first condition is true (or false).

if(percentage_obtained>=90 ):
    if percentage_obtained==90:
        print("Luckly Distinction")
    elif (percentage_obtained == 100):
        print("topper")
elif(percentage_obtained>=80 ):
    print("you have obtained first division ")
elif(percentage_obtained>=70 ):
    print("you have obtained second division ")
else:
    print("fail")

print("-----"*10)



#practice question 

# Practice Questions
# Even/Odd: Take a number and print whether it's even or odd.
# Largest of three: Take three numbers and print the largest, using nested if or elif.
# Leap year: Check if a year is a leap year (divisible by 4, but not by 100, unless also by 400).
# Grade calculator (fix the overlap bug): Take marks (0–100) and print grade A/B/C/D/F using elif only — no and needed.
# Ticket pricing: Take age and print ticket price: free (<5), $5 (5–12), $10 (13–59), $7 (60+). Use chained comparisons.
# Login check: Take a username and password, compare against fixed values using and, print "Access granted" or "Access denied."
# Traffic light: Take a color (red/yellow/green) as input and print the action (stop/wait/go) using elif.
# BMI calculator: Take weight and height, compute BMI, and print category (underweight/normal/overweight/obese) using nested if for one category split by gender.
# Ternary practice: Rewrite the vote-eligibility check in one line using a ternary expression.
#  Number sign: Check if a number is positive, negative, or zero.

# Project 1: ATM Simulator (Beginner-friendly)
# Simulate a single ATM transaction using variables, operators, and conditionals.
# Requirements:
# Store a fixed balance (e.g., 5000) and pin (e.g., 1234) as variables.
# Ask the user to enter their PIN.
# If PIN is wrong → print "Incorrect PIN" and stop.
# If PIN is correct, ask them to choose: 1 for Withdraw, 2 for Deposit, 3 for Check Balance.
# Withdraw: ask amount. If amount > balance → "Insufficient funds". Else deduct and show new balance.
# Deposit: ask amount, add to balance, show new balance.
# Check Balance: just print it.
# Bonus: withdrawal amount must be a multiple of 100, else print an error.

# Project 2: Electricity Bill Calculator
# Great for practicing operators + nested conditions.
# Requirements:
# Ask user for units of electricity consumed.
# Calculate bill using slab rates, e.g.:
# 0–100 units → ₹5/unit
# 101–200 units → ₹7/unit
# 201–300 units → ₹10/unit
# above 300 → ₹12/unit
# Add a fixed "meter charge" of ₹50.
# If total bill > ₹1000, apply a 2% surcharge.
# Print final bill.

# Project 3: Simple Quiz Game (most fun, ties it all together)
# Ask 5 questions (hardcode them), one at a time.
# Compare user's answer (string) to the correct answer using ==.
# Keep a score variable, increment with +=1 on correct answer.
# After all questions, use if/elif/else to print a result:
# score == 5 → "Perfect score!"
# score >= 3 → "Good job!"
# else → "Needs improvement"






