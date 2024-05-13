import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




# height = [1,2,3,4,5]
# weight = [2,4,6,8,10]
# plt.plot(weight, height)
# plt.hist(height) #histogram using bins
# plt.xlabel('height')
# plt.ylabel('weight')
# plt.title("Growth Projections")
# plt.scatter(weight, height, np.array(height))
# plt.text()
# plt.show()
# np_height = np.array(height)
# np_weight = np.array(weight)

# bmi = np_weight/np_height**2
# # print(bmi)

# np_2d = np.array([[1],[2]])
# print(np_2d[0,0])

# h = np.random.normal(1, 0.2, 20)
# cs = np.column_stack((np_height, np_weight))

# np.mean(np_height)
# np.median(np_height)
# np.std(np_height)

# # np.column_stack((h,h))

# print(np.corrcoef(cs))

# print(int(6.5) + True + bool("0"))
# "".replace("","cash")

# import pandas as pnd

# ru_brics = pnd.DataFrame({'Additional Name':['B.E. Krapah'],
#              'age': [20], 
#              'program':['comp eng']})

# mom_contact = pnd.read_csv(filepath_or_buffer= 'C:/Users/ACE/Documents/Bluetooth/mom.csv')

# print(mom_contact)

# a = 12
# print(int(str(a)[-2]) + int(str(a)[-1]))


# b = [1,2,3,4,5]
# for x in enumerate(b) :
#     print(x)
#     pass
# print(enumerate(b))

# ops = ['5','2']
# record = []
# for x in ops:
#     if (x >= str(-30000) and x <= str(50000)) :
#         record.append(int(x))
#         print(x)
#     else:
#         if (x == 'C'):
#             record.pop()
#         elif (x == 'D'):
#             record.append(2 * record[-1])
#         elif (x == '+'):
#             record.append(record[-2] + record[-1])
#     # print(int(x))

# result = 0
# for i in record:
#     result += i
# print(result)

plt.hist()


arr = [[1,1,1,1],
        [0,1,0,0],
        [1,1,1,0]]

inv = [1,0]
print(range(5))
# for r in range(len(arr)):
#     arr[r].reverse()
#     for c in range(len(arr)):
#         print(arr[r][c])
#         arr[r][c] = inv[arr[r][c]]
# import pandas as 
print(arr)
pd.read_csv(filepath_or_buffer="", index_col=0)
DD={"1":1}
print(DD.keys())

x = "leetcode"
found = 0
for n in range(len(x)):
        for m in range(n+1, len(x)):
                if (x[n]==x[m+1]):
                        print(n, m+1)
                        found == 1
                        break
                else:
                        continue
        if found == 0:
                print(n)
                break
        if found == 1:
                continue   
        if n == len(x) and found == 2:
                print(-1)
        
for key, val in dict.items():
        pass

cv =  np.array([[1,1,1,1],[1,1,1,1]])

#iterated nd arrays
for x in np.nditer(cv):
        pass 


#Dice game
"""
# NumPy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()
"""

"""
# numpy and matplotlib imported, seed set

# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()

# Simulate random walk 20 times
all_walks = []
for i in range(20) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand(0,1) <= 0.005 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()
"""
