import pandas as pd
import sys

filename = sys.argv[1]

df = pd.read_csv(filename)

bool_series = pd.isnull(df["sex"])

missing_cases = df.isnull().values.any()

print(missing_cases.sum())

df.info()