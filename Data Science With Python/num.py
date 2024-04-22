import numpy as np

height = [1,2,3,4,5]
weight = [2,4,6,8,10]
np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight/np_height**2
# print(bmi)

np_2d = np.array([[1],[2]])
print(np_2d[0,0])

h = np.random.normal(1, 0.2, 20)
cs = np.column_stack((np_height, np_weight))

# np.column_stack((h,h))

print(np.corrcoef(cs))

