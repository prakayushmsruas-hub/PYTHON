"""Create a NumPy array containing the marks:

85, 72, 91, 68, 79

Then calculate:

Total marks
Average marks
Highest mark
Lowest mark"""

import numpy as np

marks=np.array([85,72,91,68,79])

print(f"Sum: {np.sum(marks)}")
print(f"Avg Marks: {np.average(marks)}")
print(f"Highest Marks: {np.max(marks)}")
print(f"Lowest Marks: {np.min(marks)}")
