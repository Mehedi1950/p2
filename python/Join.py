import numpy as np
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([6,7,8,9,1,2])
print(np.stack((arr1,arr2)))
print(np.stack((arr1,arr2),axis= 1))