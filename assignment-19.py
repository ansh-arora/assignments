import numpy as np
#Q1
# a=np.array([])
# a=np.random.random((10,1))
# print(a)
# s=(np.sum(a, axis=0))
# s=s/10
# print('mean of the array is:',s)

#Q2
# a=np.array([])
# a=np.random.random((20,1))
# print(a)
# s=np.std(a)
# print('standard deviation is:',s)
# print('variance is:',s*s)

#Q3
# a=np.random.random((10,20))
# b=np.random.random((20,25))
# c=(a.dot(b))
# print(c)
# print('sum of all elements:',np.sum(c))

#Q4
# import math
# a=np.arange(1,11).reshape(10,1)
# print('array \'a\':\n',a)
# b=np.empty(shape=[10,1])
# for x in range (10):
#     s=1/(1+(math.exp(a[x,0])))
#     b[x,0]=s
# print('array \'b\':\n',b)
