import pandas as pd
import numpy as np

frame_11 = pd.DataFrame({'a': range(4), 'b': range(
    4, 0, -1), 'c': ['one', 'one', 'two', 'two'], 'd': [0, 1, 2, 3]})
print(frame_11)
frame_12 = frame_11.set_index(['c', 'd'])
print(frame_12)
frame_13 = frame_11.set_index(['c', 'd'], drop=False)
print(frame_13)
print(frame_12.reset_index())
frame_14 = frame_11.set_index(['c', 'd'], drop=False, append=True)
print(frame_14)
print('--' * 50)
stocks = pd.DataFrame(np.arange(1, 17).reshape(4, 4),  columns=[
    ['京东', '京东', '天猫', '天猫'], ['price', 'number', 'price', 'number']])
print(stocks)
print(stocks.columns)
print(stocks.index)
print(stocks.values)
print(stocks['京东', 'number'])
print('->' * 40)
mux = pd.MultiIndex.from_product([list('ab'), [2014, 2015], range(1, 3)])
df = pd.DataFrame(dict(A=1), mux)
print(df)
print(df.index.get_level_values(0))
df.index.map('{0[2]}/{0[1]}'.format)
df.index = [df.index.get_level_values(0), df.index.map('{0[2]}/{0[1]}'.format)]
print(df)


frame=pd.DataFrame(np.arange(12).reshape(4,3),
                index=[list('aabb'),list('1212')],
                columns=[['ohio','ohio','colorado'],['Green','Red','Green']])
print(frame)