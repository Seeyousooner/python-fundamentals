# Control Flow
# 5-3

alien_color = ['green', 'red', 'yellow']
if 'green' in alien_color:
    print('OVERKILL!!! YOU EARNED 5 POINTS')

# Part 2: Write one version of this program that passes the if test and another
# that fails. (The version will have no output).
if 'yellow' in alien_color:
    print('LEVEL UP')
if 'pink' in alien_color:
    print('Your alien is pink')

# 5-4

if 'pink' in alien_color:
    print(' OVERKILL!!! YOU EARNED 5 POINTS')
else:
    print('Your alien is now pink')


if 'red' in alien_color:
    print("OVERKILL!!! YOU EARNED 10 POINTS")
elif 'yellow' in alien_color:
    print("OVERKILL!!! YOU EARNED 10 POINTS")


def if_version():
    alien_colors1 = ['Green', 'Yellow', 'Red']
    if 'Green' in alien_colors1:
        print("alien is green.")
    if 'Red' in alien_colors1:
        print("alien is red.")
    if 'Yellow' in alien_colors1:
        print("alien is yellow.")

if_version()

def else_version(alien_color2):
    if alien_color2 == ['Green', 'Yellow', 'Red']:
        print("Your Alien is green. His name is Alan.")
    else:
        print("ALIEN DEAD.")

else_version('pink')

def green_alien():
    alien_color_1 = 'green'
    if 'green' in alien_color_1:
        print("Your alien is green. YOU EARNED 10 POINTS")
    elif 'yellow' in alien_color_1:
        print("YOU EARNED 10 POINTS")
    elif 'red' in alien_color_1:
        print("YOU EARNED 15 POINTS")
    else:
        print('ALIEN DEAD.')

green_alien()

def yellow_alien():
    alien_color_2 = 'yellow'
    if 'yellow' in alien_color_2:
        print("Your alien is yellow. YOU EARNED 10 POINTS")
    elif 'green' in alien_color_2:
        print("YOU EARNED 5 POINTS")
    elif 'red' in alien_color_2:
        print("YOU EARNED 5 POINTS")
    else:
        print('ALIEN DEAD')

yellow_alien()

def red_alien():
    alien_color_3 = 'red'
    if 'red' in alien_color_3:
        print("Your alien is red. YOU EARNED 15 POINTS")
    elif 'green' in alien_color_3:
        print("YOU EARNED 10 POINTS")
    elif 'yellow' in alien_color_3:
        print("YOU EARNED 5 POINTS")
    else:
        print("ALIEN DEAD.")

red_alien()

5-6

def stage_life():
    age = 12
    if age < 2:
        print('This person is a baby.')
    elif age <= 2 and age < 4:
        print('This person is a toddler.')
    elif age <= 4 and age < 13:
        print('This person is a kid.')
    elif age <= 13 and age < 20:
        print('This person is a teenager.')
    elif age <= 20 and age < 65:
        print('This person is an adult.')
    elif age > 65:
        print('This person is an elder.')

stage_life()

def q5_question(arg1):
    print(bool(arg1))

q5_question(12)
q5_question(1.2)
q5_question(0)
q5_question(0.4)
q5_question(0.0)
