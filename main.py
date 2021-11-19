import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data_2.csv')
print(df['Grade'].value_counts())
print('---------------------------------------------------')
temp = df['Category'].value_counts()
print(temp)
print('---------------------------------------------------')
print(df.groupby(by='Category')['Year'].agg(['min', 'max']))
print('---------------------------------------------------')
print(df.groupby(by='Mean Scale Score')['Year'].agg(['min','mean']))

df['Category'].value_counts().plot(kind = 'pie')
plt.show()
