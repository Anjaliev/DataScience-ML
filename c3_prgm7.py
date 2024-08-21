import pandas as pd
df=pd.read_csv('Iris.csv')
print('Shape of dataset\n',df.shape)
print('1st 5 and last 5 rows in dataset\n',df)
print('Size of dataset\n',df.size)
print('Num of samples available for each variety\n',df.count())
print('Description of dataset\n',df.describe())