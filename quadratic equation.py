import cmath
print("General Form: ax**2+bx+c=0")
a = int(input("Enter a(a!=0):"))
b = int(input("Entr b:"))
c = int(input("Enter c:"))

d = (b**2)-(4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print("\n")
print("Result for equation, {a}x**2+{b}x+{c}=0,are:-\n")

if d>0:
    print("Type of Root: Two distinct real root")
elif d==0:
    print("Type of Root: two equal real root")
elif d>0:
    print("Type of Root: two complex root")
#print(f"the solutions are {sol1} and {sol2}") #ekhane f na dile ans print hocche na kno
print("the solutions are",sol1,sol2)