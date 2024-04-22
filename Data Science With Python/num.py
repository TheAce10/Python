import numpy as nm

height = [1,2,3,4,5]
width = [2,4,6,8,10]
np_height = np.array(height)
np_width = np.array(width)

bmi = np_width/np_height**2
print(bmi)