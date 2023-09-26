import csv

import pandas as pd

df1 = pd.read_csv("scraped-data.csv")
print(df1["mass"])

data1 = []

df1["mass"] = df1["mass"]*0.102763
df1["radius"] = df1["radius"]*0.000954588

print(df1["mass"])

print(df1.describe())
print(df1.info())
print(df1.dtypes)

df1.to_csv("final_data.csv")
