import pandas as pd
import sys

filename = sys.argv[1]

df = pd.read_csv(filename)
bool_series = pd.isnull(df["sex"])


missing_cases = df.isnull().values.any()
missing_rows =  df[df.isnull().any(axis=1)]

print("INFO")
df.info()

print("=====================")

print(missing_cases)
print(missing_rows)