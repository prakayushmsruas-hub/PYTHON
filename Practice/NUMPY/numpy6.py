"""Create:

marks = np.array([45, 67, 82, 91, 56, 73])

Calculate:

Add 5 bonus marks to every student
Find the highest mark
Find the lowest mark
Find the average
Find how many students scored above 60
"""

import numpy as np
marks = np.array([45, 67, 82, 91, 56, 73])
bonus=marks+5
print(bonus)
print(np.max(marks))
print(np.min(marks))
print(np.mean(marks))
print(marks > 60)
print(marks[marks > 60])
print(np.sum(marks>60))
# count=0
# for mark in marks:
#     if mark>60:
#         count+=1
# print(f"{count} students scored above 60")        