# Write a Python program to solve quadratic equation.

import math

print("Solving Quadratic Equation")

a = int(input("Enter value of a (Co-efficient of x2) : "))
b = int(input("Enter value of b (Co-efficient of x) : "))
c = int(input("Enter value of c (constant) : "))
d = b**2 - 4*a*c

print("\n Root of quadratic equation is ",(-b + math.sqrt(d))/(2*a) , " and ",(-b - math.sqrt(d))/(2*a))