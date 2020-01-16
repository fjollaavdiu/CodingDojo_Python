def sum(a,b):
    print("a:",a,"b:",b)
    return a+b
print(sum(3,5))
print(sum(2,4)+sum(1,5))

# define a function that says hello to the name provided
def say_hello(name="bllaa"):
    if name:
        print("hello,"+name+",from inside the funstion")
    else:
        print("no name")
print("outside of the function")
