#no need to create variables, compiler does it.   x = 5
#variables can also change types without explicitly being stated
#indentations matter i.e blocks of code (also have to have the same amount of white space)
#single or double quotes can be used to declare strings

#number guessing game where user tries to guess a number within the minimum amount of guesses

import math
import random

#lower bound
lower = int(input('input lower bound - '))

#upper bound
upper = int(input('input upper bound - '))

#generate random number between bounds
x = random.randint(lower, upper)
num = math.log(upper - lower + 1, 2)
print("Try to guess in ", round(num), "tries!")

count = 0

#while loop for the guesses 
while count < num:
    count += 1

    guess = int(input("Guess a number: "))
    
    if x == guess:
        print("You got it in ", count, "tries!")
        break #from loop
    elif guess > x:
        print("Too high!")
    elif guess < x:
        print("Too low!")
    
if count >= num:
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")
