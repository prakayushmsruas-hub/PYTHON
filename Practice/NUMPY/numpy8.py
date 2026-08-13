"""Using:

marks = np.array([
    [85, 72, 91],
    [68, 79, 88],
    [92, 81, 75]
])

Row	Student	Math	Physics	Chemistry
0	Student 1	85	72	91
1	Student 2	68	79	88
2	Student 3	92	81	75

Find:

Total marks of each student
Average marks of each student
Highest mark in each subject
Average mark of each subject"""

import numpy as np
marks = np.array([
    [85, 72, 91],
    [68, 79, 88],
    [92, 81, 75]
])
# axis=0 is for row
# axis=1 is for column
print("Total Marks of each student:",np.sum(marks,axis=1))
print("Average Marks of each student:",np.mean(marks,axis=1))
print("highest Marks of each student:",np.max(marks,axis=1))
print("lowest Marks of each student:",np.min(marks,axis=1))
print("highest Marks of each Subject:",np.max(marks,axis=0))
print("Average Marks of each Subject:",np.mean(marks,axis=0))
print("lowest Marks of each Subject:",np.min(marks,axis=0))