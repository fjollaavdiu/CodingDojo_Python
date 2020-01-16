# # 1.Create a function that accepts a number as an input.  Return a new list that counts down by one, from the number (as lists 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].
# def countdown(num):
#   for x in range(num, -1, -1):
#     print([x],end=",")
# countdown(10)

# # 2.Print and Return - Your function will receive a list with two numbers. Print the first value, and return the second.
# def print_and_return(a,b):
#     print(a)
#     return b
# result = print_and_return(3,7)
# print(result)

# 3.First Plus Length - Given a list, return the sum of the first value in the list, plus the list's length.

def my_list(x):
    thesum=0
    for i in x:
        thesum=x[0]+(len(x))
    return thesum
print(my_list([1,2,3,5]))

# 4.Values Greater than Second - Write a function that accepts a list, and returns a new list with the list values that are greater than its 2nd value.  Print how many values this is.  If the list is only one element long, have the function return False

# 5.This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size, and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].