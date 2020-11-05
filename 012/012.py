import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('012/Students.xlsx', index_col='From')
print(students)

students['2017'].plot.pie(fontsize=8, counterclock=False, startangle=-270)
plt.title('Source of International Students', fontsize=16, fontweight='bold')
plt.ylabel('2017', fontsize=12, fontweight='bold')
plt.show()
