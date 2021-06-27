# -*- coding: utf-8 -*-
"""
This program asks the user to think of a number between 1 and 99, and uses a bifurcation method to guess the number.
"""
import math

answers = {
    "affirm": {"yes", "correct", "True", "1"}, 
    "up": {"+", "up", "increase", "low"}, 
    "down": {"-", "down", "decrease", "high"}
    } #dictionary containing sets of acceptable answers

print("Think of an integer between 1 and 99. I will guess it.")

guess = 50 #initial guess
increment = 25 #initial increment
ans = input("Are you thinking of the number " + str(guess) + "?: ")

while not {ans}.issubset(answers["affirm"]):
    
    if {ans}.issubset(answers["up"]):
        
        guess = int(guess + increment)
        
    elif {ans}.issubset(answers["down"]):
        
        guess = int(guess - increment)
    
    increment = math.ceil(increment/2)
    ans = input("Are you thinking of the number " + str(guess) + "?: ")
    
print("\nI win!")
