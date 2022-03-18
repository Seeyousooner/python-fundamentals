# Lab-Numbers
# 2-8

print(4 + 4)
print(32/4)
print(13-5)
print(-2*-4)

# 2-9

favorite_number = "12"
message = f"My favorite number is {favorite_number.title()}."
print(message)

# #2



def number_sets():
    va = 456_234
    vb = 6_8423_791
    vc = 13_794_628
    vd = 96_374
    print(va)
    print(vb)
    print(vc)
    print(vd)


number_sets()

# #3



def q3_question(arg1, arg2):
    print("arg1 is being converted from an int to float:", float(arg1))
    print("arg2 is being converted from a float to an int:", int(arg2))


q3_question(10, 13.5)


# #4

def favorite_movie():
    movie = input('What is your favorite movie?')
    times_seen = input('How Many times have you seen it?')
    message1 = 'My favorite movie is {0} and I have seen it {1} times'
    print(message1.format(movie, times_seen))


favorite_movie()


