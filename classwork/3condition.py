#Conditional statements help you execute certain blocks of code only when specific condition are true.

#If  else statement - 
# if(condition):
# statement

# The if statement is used to make decisions in a program.
# It checks a condition:
    # If the condition is True, the code inside the if block runs.
    # If the condition is False, the code inside the if block is skipped.
age= int(input("enter your age"))
if (age>=18):
    print("You can vote ")
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


# nested if 
percentate  = 90 





