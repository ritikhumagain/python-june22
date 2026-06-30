#for loop
for i in range(5):
    print("hello World",i)
    
print("--------"*5)
for i in range (10,0,-2):
    print("hello world",i)

print("------"*5)
table_number = int(input("enter the number "))
for i in range(0,11,1):
    print(f"{table_number} x {i} =",table_number*i)

print("------"*5)
a = "hello "
for i in a : 
    print("Python")
print("------"*5)
a = "Hello World . I am python."
for i in a : 
    print(i , end = "")
print("------"*5)
a = "Hello World . I am python."
for i in a : 
    if i != ".":
        print(i , end= "")

#Control statement 
# break
# continue
# continue

for i in range (10 ): 
    if i == 5 : 
        break
    print(i )

for i in range(10 ): 
    if (i == 5):
        continue
    print(i)

a = "Hell0 world . iam python . "
for i in a : 
    if i (i != ". " ):
        break
    print(i , end = "")




a = "Hell0 world . iam python . "
for i in a : 
    if i (i != ". " ):
        break
    print(i , end = "")



a = "Hell0 world . iam python . "
for i in a : 
    if i (i != ". " ):
        continue
    print(i , end = "")






a = 0 
while (a<5):
    print("hello world")
    a+= 1

i = 1 
x = int(input("Enter x = 2 "))