#string 
# 1 . Strings are everywhere: usernames, passwords, file paths, JSON data, API responses,log messages, user input, HTML/CSS, SQL queries, chat messages. 
s1 = 'hello'
s2 = "hello"
s3 = '''multi
line
string'''
s4 = "It's a test"      # use double quotes when text has an apostrophe
s5 = type(str(123)   )
print(s1,s2,s3,s4,s5)        # convert other types to string
print("-------"*5)


# 2.  EscapeMeaning, \n-newline ,   \t-tab,  \\-backslash,    \' \"-quote
print("Line1\nLine2\tTabbed")
print("-------"*5)


# 3. Strings Are Immutable
# You cannot change a string in place. Every "modification" creates a new string.
name = "python"
# name[0] = "P"     # ❌ TypeError
name = "P" + name[1:]   # ✅ create a new string 
print(name)


# 4. Indexing & Slicing 
#for indexing we use variable name and []
# Indexing means accessing one element at a specific position. positive indexing start from left and negative indexing start from right side
s = "Programming"
s[0]        # 'P'          → first char
s[-1]       # 'g'          → last char
# print(s[20])   # ERROR


# 2. What is Slicing?--Slicing means taking multiple characters from a string.
# syntax -- variable[start:stop:step]  start include but stop exclude
s[0:4]      # 'Prog'       → slice [start:stop)
s[:4]       # 'Prog'   it assume that it will start from start
s[4:]       # 'ramming'   it assume that it will end at lenofstring
s[::2]      # 'Pormig'     → every 2nd char
s[::-1]     # 'gnimmargorP' → reverse a string (very common interview trick)
print("------"*5)

# 🔍 Searching & Checking
s = "Hello World"
print(s.find("World")  )      # 6  (index, or -1 if not found)
print(s.index("World") )      # 6  (like find, but raises error if missing)
print(s.count("l")     )      # 3
print(s.startswith("Hello") ) # True
print(s.endswith(".py"))      # True — very common for checking file types
"World" in s           # True


# Cleaning User Input (form validation, file parsing)
"  hello  ".strip()      # 'hello'   remove whitespace both ends
"  hello  ".lstrip()      # 'hello  '
"  hello  ".rstrip()      # '  hello'
"hello".strip("h")        # 'ello'    strip specific chars

# 🔠 Case Handling (login systems, comparisons)
"Hello".upper()        # 'HELLO'
"Hello".lower()        # 'hello'
"hello world".title()  # 'Hello World'
"Hello".swapcase()     # 'hELLO'
"hello".capitalize()   # 'Hello'

# ✂️ Splitting & Joining (parsing CSV, logs, sentences — extremely common)
"a,b,c".split(",")            # ['a', 'b', 'c']
"one two three".split()       # ['one', 'two', 'three']  (splits on whitespace)
"line1\nline2".splitlines()   # ['line1', 'line2']
"-".join(["a", "b", "c"])     # 'a-b-c'

# 🔁 Replacing
"I like cats".replace("cats", "dogs")   # 'I like dogs'

# ✅ Validation checks (form/input validation)
"123".isdigit()     # True
"abc".isalpha()     # True
"abc123".isalnum()  # True
"   ".isspace()     # True
"HELLO".isupper()   # True
"hello".islower()   # True

# 🎨 Formatting output (reports, dashboards, messages)
name, age = "Sam", 25
# f-strings (modern, preferred — use this in your projects)
print(f"{name} is {age} years old")
print(f"{3.14159:.2f}")        # '3.14'   round to 2 decimals
print(f"{5:04d}")              # '0005'   zero-padded number
print(f"{name:>10}")           # right align in 10-char width
# .format() (older style, still seen in existing codebases)
print("{} is {} years old".format(name, age))
# % formatting (legacy, seen in older code / logging)
print("%s is %d years old" % (name, age))

