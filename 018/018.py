import pandas as pd

employees = pd.read_excel("018/Employees.xlsx", index_col = 0)  # source index_col = 'ID'
df = (employees['Full Name'].str.split(expand=True))
employees['First Name'] = df[0]
employees['Last Name'] = df[1].str.upper()
print(employees)
print(f'df is type = {type(df)}')
