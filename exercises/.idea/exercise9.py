# Classes and Functions
# 8-3

from typing import List


def make_shirt(size, message):
    print('The shirt you ordered is a', size, 'and it says', message)


make_shirt('small', '"You Just Got Corduroyed!"')


make_shirt(size='small', message='"You Just Got Corduroyed!"')

# 8-4

def make_shirt1(size='large', message='Memes Are Dead'):
    print('The shirt you ordered is a', size, 'and the message is', message)


make_shirt1()
make_shirt1(size='medium')
make_shirt1(size='small', message='You Just Got Corduroyed!')

# 8-5

def describe_city(city_name, city_country='USA'):
    print(city_name, 'is in', city_country)


describe_city('Haysville')
describe_city('Andover')
describe_city('Katowice', 'Russia')


# 8-9

def show_messages(text_message):
    for message in text_message:
        print(message)


text_messages = ['Today is the 17th.', 'Tommorow is the 18th.', 'The next day is the 19th.']
show_messages(text_messages)

# 8-10

def show_messages(text_message):
    print('These are the text messages.')
    for message in text_message:
        print(message)


def send_messages(text_messages, sent_messages):
    print('These are the messages for sent messages.')
    while text_messages:
        draft_messages = text_messages.pop()
        print(draft_messages)
        sent_messages.append(draft_messages)


text_messages = ['Today is the 17th.', 'Tommorow is the 18th.', 'The next day is the 19th.']
sent_list = [text_messages]

sent_messages = []
send_messages(text_messages, sent_messages)
print(text_messages)
print(sent_messages)

# 8-11
send_messages(text_messages[:], sent_messages)

# 9-1, 9-2, 9-3
# 9-1

class Restaurant:
    def __init__(self, restaurant_name, type):
        self.restaurant_name = restaurant_name
        self.type = type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


restaurant = Restaurant("Rene's", "Mexican Food")
restaurant.open_restaurant()
print(f"{restaurant.type}")
print(f"{restaurant.restaurant_name}")

# 9-2

class Restaurant:
    def __init__(self, restaurant_name, type):
        self.restaurant_name = restaurant_name
        self.type = type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


restaurant_1 = Restaurant("Rene's", "Mexican Food")
restaurant_2 = Restaurant("Walts's", "American Food")
restaurant_3 = Restaurant("Saigon's", "Asian Food")

restaurant_1.open_restaurant()
print(f"{restaurant.type}")
print(f"{restaurant.restaurant_name}")

restaurant_2.open_restaurant()
print(f"{restaurant.type}")
print(f"{restaurant.restaurant_name}")

restaurant_3.open_restaurant()
print(f"{restaurant.type}")
print(f"{restaurant.restaurant_name}")

# 9-3

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(self.first_name, self.last_name)
        print()
    def greet_user(self):
        print(f"Hello, {self.first_name}")


new_user = User("Evan", "Steiner")
new_user.describe_user()
new_user.greet_user()

# 9-5

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(self.first_name, self.last_name)
        print()
    def greet_user(self):
        print(f"Hello, {self.first_name}")
    def increment_login_attempts(self):
            self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
            self.login_attempts = 0



new_user = User("Evan", "Steiner")
new_user.reset_login_attempts()
print(f"login attempts: {new_user.login_attempts}")

