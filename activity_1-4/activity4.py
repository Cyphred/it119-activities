import pandas as pd
import sys

filename = sys.argv[1]

df = pd.read_csv(filename)

null_count = df.isnull().sum()

print("Found " + str(null_count) + " records with null values")