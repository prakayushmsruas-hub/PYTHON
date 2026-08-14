"""Try this:

import numpy as np
marks = np.array([25, 45, 67, 32, 89, 76, 18, 55])

Use np.where() to print "Pass" for marks ≥ 40 and "Fail" otherwise.
Use np.where() to give 5 bonus marks to students who scored ≥ 60, otherwise give their original marks.
Use np.where() to replace marks below 30 with 0."""

import numpy as np
marks = np.array([25, 45, 67, 32, 89, 76, 18, 55])
print(np.where(marks>=40,"Pass","Fail"))
print(np.where(marks>=60,marks+5,marks))
new_marks = np.where(marks < 30, 0, marks)
print(new_marks)

