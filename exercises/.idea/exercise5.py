# Operators
# 5-1
# Write a series of conditional tests. Print a statement describing each test
# and your prediction for the results of each test.

# Conditional Test 1 (True)
batcave = 'cave'
print("Is batcave == 'cave'? I predict true")
print(batcave == 'cave')

# Conditional Test 2 (False)
batcave = 'apartment'
print(" Is batcave == 'cave'? I predict false because it is case sensitive")
print(batcave == 'Apartment')

# Conditional Test 3 (True)
batcave = 'home'
print(" Is batcave =='home'? I predict true.")
print( batcave == 'home')

# Conditional Test 4 (True)
Evan = 34
cody = 10


def who_is_taller():
    result1 = Evan > cody
    print(" Is Evan taller than cody? I predict true.")
    print(result1)


who_is_taller()

# Conditional Test 5 (False)
cody = 6
curtis = 9


def who_is_taller():
    result2 = curtis > cody
    print(" Is curtis taller than cody? I predict true.")
    print(result2)


who_is_taller()


# Conditional Test 6 (False)
def who_is_taller():
    result3 = curtis >= Evan
    print(" Is curtis the same height as Evan? I predict false.")
    print(result3)


who_is_taller()

# Conditional Test 7 (True)
result4= Evan >= 21 and curtis <=7
print("Is Evan taller than 21? Is curtis shorter than 7? I predict true.")
print(result4)

# Conditional Test 8 (False)
result5= cody >=10 and curtis >=9
print(" Is cody taller than 10? Is curtis taller than 9? I predict false.")
print(result5)

# Conditional Test 9 (False)
favorite_color =['pink', 'purple']
print( "Is black one of Evan's favorite colors? I predict false.")
print( 'black' in favorite_color)

# Conditional Test 10 (False)
color = 'yellow'
if color not in favorite_color:
    print("Is yellow one of Evan's favorite colors? I predict false")
    print('yellow' in favorite_color)


#  5-2 Question 2

# Tests for equality with strings (True)
result3 = "Evan Steiner is a twink" == "Evan Steiner is a twink"
print("This is for equality with strings.Is Evan Steiner a mom? I predict true.")
print(result3)

# Tests for inequality with strings (False)
result4 = "Evan Steiner is a hunk" != "Evan Steiner is a hunk"
print("This is for inequality with strings. Is Evan Steiner a hunk? I predict false.")
print(result4)

# Test using lower() method (True)
color = 'Yellow'
print("This is for the lower method:", color.lower == 'Yellow')

# Test using lower() method (False)
print("This is for the lower method:", 'Yellow' == color.lower)

# Numerical tests (False)
# equality
result6 = (Evan == cody)
print("This is for the equality one:", result6)

# inequality (True)
result7 = (Evan != cody)
print("This is for the inequality one:", result7)

# great than (True)
result8 = (Evan > cody)
print("This is for the greater than one:", result8)

# less than (False)
result9 = (curtis > cody)
print("This is for the less than one:", result9)

# greater than or equal to (False)
result10 = (curtis >= cody)
print( "This is for the greater than or equal to one:", result10)

# less than or equal to (True)
result11 = (curtis <= curtis)
print("This is for the less than or equal to one:", result11)


# keyword and (True)
result12= cody >=5 and curtis >=5
print("This is for the 'and' keyword:", result12)

# keyword or (False)
result13= cody >= 10 or curtis >=10
print("This is for the 'or' keyword:", result13)

# (True)
friends = ['cody', 'curtis']
print("Is cody one of Evan's friends?", 'cody' in friends)

# Whether an item is not on a list (False)
print("Is curtis one of Evan's friends?", 'curtis' in friends)


def Evan_friends(friend1, friend2):
    result1 = friend1 * friend2
    print(result1)


Evan_friends(9, 6)


def Evan_friends(friend1, friend2):
    result2 = friend1 / friend2
    print(result2)


Evan_friends(10, 2)


def Evan_friends (friend1, friend2):
    result3 = friend1 % friend2
    print(result3)


Evan_friends(20, 8)


def Evan_friends(friend1, friend2):
    result4 = friend1 ** friend2
    print(result4)


Evan_friends(6, 3)


# Question 4

def assignment_operator(value):
    value %= 5
    print(value)


assignment_operator(10)


# exponent equals
def assignment_operator(value):
    value **= 5
    print(value)


assignment_operator(11)


# plus equals
def assignment_operator(value):
    value += 8
    print(value)


# minus equals
def assignment_operator(value):
    value -= 6
    print(value)


assignment_operator(12)
