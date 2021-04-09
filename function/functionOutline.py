'''
This outline will help solidify concepts from the Functions lesson.
Fill in this outline as the instructor goes through the lesson.
'''


#1) Make a function that has two boolean parameters. If both booleans are
#true, return true. Else, return false. Then, call the function.
#Print what the function returns.

def trueToFalse(t, c):

    if (t + c):
        True
    else:
        False
    
    
trueToFalse(True)

print(True)
#2) Make a function that takes one int parameter: gallons. Convert gallons
#to cups (do this by multiplying gallons by 16). Then return cups. Then,
#call the function.
#Print what the function returns.

def gallonsToCups(gallons):

    cups = gallons * 16
    
    return cups

gallonsToCups(16)

print(16)

#3) Make a function of any any kind with a common SYNTAX error. Then, call the
#function.
#Print what the function returns.

def sumTwoNums(numOne, numTwo):
    sum = numOne + numTwo
    
a = 2
z = 4
num = sumTwoNums(a, z)

print(num)
