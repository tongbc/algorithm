import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
b = (np.max(a,axis=1))
print(np.shape(a))
nums = (a-b.reshape(-1,1))
exnum = np.exp(nums)
denominator = 1/np.sum(exnum,axis=1)
x = exnum/np.reshape(denominator,(-1,1))
print(x)