""""
x = 10
y = 20
temp = x
print("the value of temp variable is",temp)
x = y
print("the value of x is",x)
y = temp
print("the value of y is",y)
"""

x = 10
y = 20
x,y = y,x
print("the value of x is",x)
print("the value of y is",y)