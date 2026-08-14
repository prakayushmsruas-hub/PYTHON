"""Using:

marks = np.array([
    [80, 75, 90],
    [65, 88, 72],
    [91, 60, 85]
])

Try to:

Print the first row.
Print the second column.
Print 88.
Print the last row.
Change 60 to 70.
Print all marks greater than 80."""

import numpy as np
marks = np.array([
    [80, 75, 90],
    [65, 88, 72],
    [91, 60, 85]
])
print(marks[0])
print(marks[:,1])
print(marks[1][1])
print(marks[-1])
marks[-1][-2]=70
print(marks[marks>80])
print(marks)