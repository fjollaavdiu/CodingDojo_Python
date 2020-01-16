# Create beCheerful().  Within it, print string "good morning!" 98 times.

# def beCheerful(name='', repeat=98):
#     print(f"goodmorning{name}\n"*repeat)
# beCheerful()
# beCheerful(name="fjolla", repeat=98)

# As part of this assignment, please create a function randInt() where

# randInt() returns a random integer between 0 to 100
# randInt(max=50) returns a random integer between 0 to 50
# randInt(min=50) returns a random integer between 50 to 100
# randInt(min=50, max=500) returns a random integer between 50 and 500
# Create this function without using random.randInt() but you are allowed to use random.random().


def randInt(min=0, max=100):
    import random
    num = random.random()*(max-min) + min
    return(int(num))


print(randInt())
print(randInt(min=50, max=50))
print(randInt(min=50, max=100))
print(randInt(min=50, max=500))

