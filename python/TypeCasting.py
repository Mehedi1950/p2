import numpy as np
data = np.array([ ["Enamul",1611,200.30], ["Mehedi",1844,100.50], ["Haq",1788,150.78], ["Rana",1756,20.50]])
print(data)
print(data.dtype)
id = data[:,1].astype(int)
print(id)
print(id.dtype)
salary = data[:,2].astype(float)
print(salary)
print(salary.dtype)
