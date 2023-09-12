import pandas as pd

sampledata = {
    "Name": ["Jeremy","Chrismer","Jasper","Badong","Manoy"],
    "Age": [23,25,22,72,12],
    "Rating": [2.3, 1.7, 3.0, 5.0, 5.0],
}

# Alias data frame function
df = pd.DataFrame(data=sampledata)

mean = df.mean(numeric_only=True)

median = df.median(numeric_only=True)

mode = df.mode(numeric_only=True)

std_dev = df.std(numeric_only=True)

skew = df.skew(numeric_only=True)

print("Mean values in the distribution")
print(mean)
print()

print("Median values in the distribution")
print(median)
print()

print("Mode values in the distribution")
print(mode)
print()

print("Standard deviation in the distribution")
print(std_dev)
print()

print("Skweness in the distribution")
print(skew)
print()

# Activity 1
# - Create a data frame
# - Store sample data in frame
# - Identify mean median and mode
# -  - Mode most frequent
# - Standard deviation
# - Hard coded data

# Activity 2
# File reading

# Activity 3
# Display and show which data has null values

# Activity 4
# Total number of records that have null values