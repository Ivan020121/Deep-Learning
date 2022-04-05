'''
Created on Apr 5, 2022
@author: Ivan Li
'''

# 打印 文档信息
print(__doc__)

# 导入 numpy库
import numpy as np
# 导入 time库
import time

# 创建 数组A
a = np.array([1, 2, 3, 4])
print(a)# [1 2 3 4]

# 计算两次操作花费时间
a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()

print('Vectorized version: ' + str(toc-tic))# Vectorized version: 0.007390022277832031

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()

print('For loop: ' + str(toc - tic))# For loop: 0.4368112087249756