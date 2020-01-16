# 1.Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def makeItBig(array):
    for num in array:
        if num<0:
            print('big')
        else:
            print(num)
f=makeItBig([-1,2,5,-5])
print([f])