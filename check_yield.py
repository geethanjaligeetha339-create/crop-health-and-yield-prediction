import pandas as pd

file = "dataset/yield2018/yieldsFromRaster.xlsx"

df = pd.read_excel(file)

print("Columns:")
print(df.columns)

print("\nFirst 10 rows:")
print(df.head(10))

print("\nDataset shape:")
print(df.shape)