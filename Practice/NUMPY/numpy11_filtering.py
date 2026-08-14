"""Try this:

import numpy as np
data = np.array([10, 25, 30, 45, 50, 65, 70, 85, 90, 100])

Do these:
Print all values greater than 50.
Print all values less than 40.
Print values between 30 and 80.
Print values greater than 80 OR less than 20.
Replace all values greater than 80 with 0."""

import numpy as np
data = np.array([10, 25, 30, 45, 50, 65, 70, 85, 90, 100])
print(data[(data>50)])
print(data[(data<40)])
print(data[(data>30) & (data<80)])
print(data[(data<20) | (data>80)])

data[(data>80)]=0
print(data)