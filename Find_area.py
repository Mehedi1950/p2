a = float(input("Enter first side:"))
b = float(input("Enter second side:"))
c = float(input("Enter third side:"))
d = float(input("Enter the height:"))
e = float(input("Enter the base:"))

area = (d*e)/2
s = (a+b+c)/2 #semi_perimeter
print("The area of the triangle = %.2f " %area)
print("The semi perimeter of the triangle = %.2f" %s)
import math
area1 = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area1 of the triangle = %.2f" %area1)