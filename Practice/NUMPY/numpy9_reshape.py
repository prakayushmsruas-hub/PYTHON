"""numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

Reshape it into:

1. 3 rows × 4 columns

Then:

2. 4 rows × 3 column"""

import numpy as np
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
print(numbers.reshape(3,4))
print(numbers.reshape(4,3))
