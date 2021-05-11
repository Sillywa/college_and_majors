import pandas as pd


top = pd.read_csv("lastCategory.csv")
second = pd.read_csv("../majorSchool.csv")

df = pd.merge(top, second, left_on="code", right_on="parent_code")
print(df.head())
data = df.loc[:, ['code', 'college']]
data.to_csv("majorScool.csv", index=False)