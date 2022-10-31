# Write a Python program to swap two variables without temp variable.

a = int(input("enter value of a  = "))
b = int(input("enter value of  b = "))

print("\nBefore swapping a = ",a," b = ",b)

a,b =b,a
print("After swapping a = ",a," b = ",b)


