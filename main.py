print("❤️💚") # Ctrl + Alt + N
# Open terminal = Ctrl + J

with open("data.txt", 'w', encoding="utf8") as file:
    print("❤️💚💙", file=file)

#------------------------------------------------------
# variable - Ctrl + /
"""
line 1
line 2
line 3
line 4
line 5
"""
_ = 23
print(_)

# type of value
print(type(0j)) # a + bi i^2 = -1

# Declare a constant
PI = 3.14159265
a = 300 # [-5, 256]

# full_name. age. is_over_18, user_name, ....
print(...)

#abcxyz - DO NOT
# Operators
"""
+, -, *, /, //, **, %
>, <, >=, <=, ==, != => bool (True/False)
not > and > or
falsy: 0, 0.0, 0j, None, '', [], set(), (), {}, Fraction(0, 1)
expr1 and|or expr2
if expr1 => bool(expr1) = True then and => expr2 else expr1
if expr1 => bool(expr1) = True then or  => expr1 else expr2
not => bool (True/False)
"""
# Ctrl + X
print(4 / 3) # / => float
print(4 // 3) # // => int
print(.5 > 1) # False

print('a' > 'b') # ord('a') > ord('b') <=> 97 > 98 = False

print(1 and 2)
print(0 and 2)

print('' or None)
print('Anna' or 'Beta')

print(not '') # True
print(not 1) # False

# f-strings, format(), str(), float(), int(), bool()
age = 34

print(f"I am {age}") # Shift + Alt + Down Arrow
print("I am {}".format(age)) # Shift + Alt + Down Arrow
print("I am " + str(age))

print(float(age))

print(int(True)) # 1
print(int(False)) # 0

print(bool(None)) # False
print(bool(1))

# list: [,,,,,]
int_numbers = [1, 3, 2, -10]
# friends = ["Bob", 2, "Kenny"] - DO NOT
print(int_numbers[0])
print(int_numbers[-1])

# len
print(len(int_numbers))

# append
int_numbers.append(100)
print(int_numbers)

# extend
int_numbers.extend([10, 100, 1000])
print(int_numbers)

# remove
int_numbers.remove(100)
print(int_numbers)

# remove index - 2
int_numbers.pop(2)
print(int_numbers)

# reverse
int_numbers.reverse()
print(int_numbers)

# sort
int_numbers.sort(reverse=True)
print(int_numbers)

# count
#      0  1  2  3  4  5  6
#     -7 -6 -5 -4 -3 -2 -1 
lst = [1, 2, 1, 1, 3, 4, 2]
number1s = lst.count(2)

print(number1s)

# index
idx_3 = lst.index(3)
print(idx_3)
print(idx_3 - len(lst))

# reverse by list slicing
# list slicing => new list # list
print("origin:", lst)
new_lst = lst[::-1]
print("after: ", new_lst)

print(lst[1:-1])
