# # 1.Basic - Print all the numbers/integers from 0 to 150.
# for numbers in range(0,151):
#     print("integer-",numbers)


# # 2.Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
# for multiples in range (5,1000000,5):
#     print("Check",multiples)

# # 3.Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
# for counting in range (1,100):
#     if counting % 5 ==0:
#         print("Coding")
#     elif counting % 10 == 0:
#         print ("Dojo")

# # 4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

# n=int(input("Enter n value:"))
# sum=0
# for i in range(1,n+1,2):
#     sum+=i
# print(sum)

# # 5.Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
# for countdown in range(2018,0,-4):
#     print("test-",countdown)

# 6.Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
def flexibleCountdown(lowNum, highNum, mult):
    for i in range (lowNum, highNum):
        if i % mult == 0:
            print(i)
