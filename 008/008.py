from numpy import random
import pandas as pd
import os
import numpy as np
# def validate_age(a):
#     return 18 <= a <= 30


# def level_b(s):
#     return 60 <= s < 90


students = pd.read_excel("008/Students.xlsx", index_col=0)
# students = students.loc[students['Age'].apply(validate_age)].loc[students.Score.apply(level_b)]  # 两种语法

students = students.loc[students['Age'].apply(
    lambda x: 18 <= x <= 30)].loc[students.Score.apply(lambda x: 60 <= x < 90)]
print(students)

arr2d =  np.arange(12).reshape(3, 4)

print(arr2d)
print(f'arr2d is ndim = {arr2d.ndim}')

rd_arr = np.random.randn(1, 6).reshape(2, 3)
print(rd_arr)

rd_ar2d = np.random.mtrand.randn(60).reshape(2, 30)
print(rd_ar2d)
