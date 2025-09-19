import pandas as pd


df = pd.read_csv('details.csv')
salaries = df['salary']

print(list(salaries))
