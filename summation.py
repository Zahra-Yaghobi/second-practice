# Programmer : Zahra Yaghubi
import math
import sys
total = 0
print('Summation numbers')
total = 0
while True:
    number = int(input("Enter a number or 0 to Exit: "))
    total = total + number
    if number == 0:
        break
print ("The total number is", total)  