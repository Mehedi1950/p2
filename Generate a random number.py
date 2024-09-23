"""import random
num = random.randint(0,10)
print(num)"""

"""x = 40
x = "Bangladesh"
print(x)
print(type(x))"""

square = lambda x: x * x
print(square(5))
x = lambda a,b:a**b
print(x(5,6))
y = [1,3,4,6,7]
y = list(map(lambda ab: ab**ab,y))
print(y)

numbers = [1,3,5,6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
