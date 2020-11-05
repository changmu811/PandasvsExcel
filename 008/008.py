import pandas as pd
import os

def validate_age(a):
    return 18 <= a <= 30


def level_b(s):
    return 60 <= s < 90


students = pd.read_excel('008/Students.xlsx', index_col='ID')
students = students.loc[students['Age'].apply(validate_age)].loc[students.Score.apply(level_b)]  # 两种语法
print(students)
