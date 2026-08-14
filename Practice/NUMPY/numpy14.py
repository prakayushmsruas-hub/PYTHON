"""Try this:
import numpy as np


marks = np.array([78, 45, 92, 67, 88, 55, 73])

Do:

Sort the marks in ascending order.
Sort the marks in descending order.
Find the highest 3 marks using sorting.
Find the lowest 3 marks using sorting."""

import numpy as np
marks = np.array([78, 45, 92, 67, 88, 55, 73])
print("Ascending",np.sort(marks))
print("Descending",np.sort(marks)[::-1])
print("Top 3 marks",np.sort(marks)[-3:])
print("Lowest 3 marks",np.sort(marks)[:3])