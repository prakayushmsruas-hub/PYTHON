"""Create the 2D array:

10 20 30
40 50 60
70 80 90

Then print:

10
60
80
The first row
The second column
The last row
The first two rows"""

import numpy as np

arr = np.array([[10, 20, 30], 
                [40, 50, 60], 
                [70, 80, 90]])
print(arr[0,0])
print(arr[1,2])
print(arr[2,1])
print(arr[0])
print(arr[:,1])
print(arr[2])
print(arr[0:2])


