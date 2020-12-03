import pandas as pd

products = pd.read_excel('List.xlsx', index_col='ID')
products.sort_values(by=['Worthy', 'Price'], ascending=[
                     True, False], inplace=True)
print(products)
cs = pd.read_excel('List.xlsx')
print(cs.sort_index())