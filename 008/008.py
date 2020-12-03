import numpy as np
import pandas as pd
import os
# def validate_age(a):
#     return 18 <= a <= 30
# https://lsp.readthedocs.io/en/latest/#cc

# def level_b(s):
#     return 60 <= s < 90

print(os.getcwd())
students = pd.read_excel("./Students.xlsx", index_col=0)
# print(students.head())
# students = students.loc[students['Age'].apply(validate_age)]
# .loc[students.Score.apply(level_b)]  # 两种语法
print("*" * 60)
print((students.loc[students['Age'].apply(
    lambda x: 18 <= x <= 30)]))
students = students.loc[students['Age'].apply(
    lambda x: 18 <= x <= 30)].loc[students.Score.apply(lambda x: 60 <= x < 90)]
print(students)

arr2d = np.arange(12).reshape(3, 4)

print(arr2d)
print(f'arr2d is ndim = {arr2d.ndim}')

rd_arr = np.random.randn()
print(rd_arr)

rd_ar2d = np.random.randn(5, 3)
print(rd_ar2d)
ar = np.arange(12)
ar2 = np.reshape(ar, (3, 4))
print(ar2)


class mymeta(type):
    def __init__(self, a, b, c):
        print(self)
        print(a)
        print(c)
        print(b)

    def __call__(self, *args, **kwargs):
        obj = object.__new__(Foo)
        self.__init__(obj, *args, **kwargs)
        return obj


class Foo(metaclass=mymeta):
    def __init__(self, name):
        self.name = name
        print(self.name)


foo = Foo("Python")
print(foo.__dict__)
print('---------------------------')


class obj_slice(object):
    def __init__(self):
        self.cache = [1, 2, 3, 4, 5, 6, 7]

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            self.cache[key] = value

    def __getitem__(self, key):
        print("__getitem__ ", type(key))
        print(
            f"key.start={key.start} key.stop = {key.stop} key.step={key.step}")
        return self.cache[key]

    def __delitem__(self, key):
        pass


ob = obj_slice()
ob[0:4:2] = ['a', 'b']
print(ob[0:5:2])
print(ob.__dict__)
