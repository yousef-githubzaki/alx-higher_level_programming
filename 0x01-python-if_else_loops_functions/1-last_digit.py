#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)

mod= number %10 if number > 10 else number %-10
print("last digit of {:d}  is {:d} a ".format(number,mod),end="")
if mod >5 :
    print("and is greater than 5")
elif mod == 0:
    print("0")
else:
    print("and is less than 6 and not 0")
