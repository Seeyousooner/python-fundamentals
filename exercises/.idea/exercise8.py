# Collections
# 5-8
usernames = ['fisk', 'peter', 'venom', 'sandman', 'admin']
for user_name in usernames:
    if user_name == 'admin':
        print("Hello admin. Not you again.")
    else:
        print("Hello", user_name, ". Welcome back loser")

# 5-9

usernames_1 = []
if usernames_1:
    for user_name1 in usernames_1:
        if user_name1 == 'admin':
            print('Hello admin. Not you again.')
else:
    print("Literally no one is here")

# 5-10
current_users = ['sonic', 'eggman', 'megaman', 'amy', 'yourmom']
new_users = ['sonic', 'eggman', 'donaldduckr', 'garfield', 'jimmyneutronlol']
lower_case_users = [user.lower() for user in current_users]
for new_user1 in new_users:
    if new_user1.lower() in lower_case_users:
        print("The username:", new_user1, "is not available.")
    else:
        print("The", new_user1, "is available.")

# 5-11
# Each result on a separate line.

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for ordinal in ordinal_numbers:
    if ordinal == 1:
        print('1st')
    elif ordinal ==2:
        print('2nd')
    elif ordinal == 3:
        print('3rd')
    else:
        print(ordinal, 'th')

# 6-1
brother_info = {'first.name': 'Brandon', 'last.name': 'Steiner', 'age': 24, 'city': 'Kansas City'}
print(brother_info['first.name'])
print(brother_info['last.name'])
print(brother_info['age'])
print(brother_info['city'])

friend_info1 = {'first.name': 'Cody', 'last.name': 'Galcia', 'age': 20, 'city': 'Wichita'}
friend_info2 = {'first.name': 'Santos', 'last.name': 'Urbina', 'age': 20, 'city': 'Wichita'}
people = (brother_info, friend_info1, friend_info2)
for person in people:
    first_name = person['first.name']
    last_name = person['last.name']
    age = person['age']
    city = person['city']
    print(first_name, last_name, 'is', age, 'years old and was born in', city, ',' ' Kansas.')