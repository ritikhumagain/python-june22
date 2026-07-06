# 1.LIST
# A list is your go-to container when you have a collection of items that can
# changemjjjjj — add, remove, reorder, update. Shopping carts, to-do apps, student
# records, search results, queues of tasks, game inventories, chat message history A list is your go-to container when you have a collection of items that can
# change — add, remove, reorder, update. Shopping carts, to-do apps, student
# records, search results, queues of tasks, game inventories, chat message history 


# 2. Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
empty = []
nested = [[1, 2], [3, 4]]          # list of lists — e.g. a grid/matrix


# 3. Lists Are Mutable (this is the BIG difference from strings)
fruits = ["apple", "banana", "cherry"]
fruits[0] = "mango"       # ✅ allowed! Lists CAN be changed in place
print(fruits)             # ['mango', 'banana', 'cherry']
# Contrast with strings where name[0] = "P" gave an error. This mutability is why
# lists are used for things that grow/shrink/change over the life of a program
# (e.g., a shopping cart where items get added and removed).


# 4. Indexing & Slicing (same rules as strings)
nums = [10, 20, 30, 40, 50]
nums[0]        # 10
nums[-1]       # 50
nums[1:3]      # [20, 30]
nums[:3]       # [10, 20, 30]
nums[::2]      # [10, 30, 50]
nums[::-1]     # [50, 40, 30, 20, 10]   reverse


# 5. Core List Methods (grouped by real use-case)
# ➕ Adding items
cart = ["apple"]
cart.append("banana")          # add ONE item to the end → ['apple', 'banana']
cart.extend(["cherry", "date"]) # add MULTIPLE items → ['apple','banana','cherry','date']
cart.insert(1, "mango")        # insert at a specific position (index 1)

# ➖ Removing items
cart.remove("banana")     # removes by VALUE (first match)
cart.pop()                # removes and RETURNS last item (great for stacks/undo)
cart.pop(0)                # removes and returns item at index 0
del cart[0]                # removes by index, no return value
cart.clear()               # empty the whole list

# 🔍 Searching
nums = [10, 20, 30, 20]
nums.index(20)       # 1   → index of FIRST match
nums.count(20)        # 2   → how many times 20 appears
20 in nums             # True → membership check

# 🔃 Sorting & Reversing
nums = [5, 2, 8, 1]
nums.sort()                    # sorts IN PLACE (changes original), ascending
nums.sort(reverse=True)        # descending
nums.reverse()                 # reverses in place
# sorted() — does NOT change original, returns a NEW list (useful when you
# still need the original order elsewhere)
original = [5, 2, 8, 1]
new_list = sorted(original)

# Copying (a classic beginner trap!)
a = [1, 2, 3]
b = a               # ❌ b is NOT a copy — both point to the SAME list
b.append(4)
print(a)            # [1, 2, 3, 4]  <- a changed too! surprising bug source

c = a.copy()        # ✅ real copy
# or: c = a[:]
c.append(99)
print(a)            # unaffected



# 6. Looping Through Lists
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# enumerate() shows up constantly — e.g. printing a numbered menu, or updating an
# item at a known position while looping.
for index, fruit in enumerate(fruits):     # when you need BOTH index and value
    print(index, fruit)



# 7. Other Useful Built-ins on Lists
nums = [4, 2, 9, 1]
len(nums)      # 4
sum(nums)      # 16
max(nums)      # 9
min(nums)      # 1