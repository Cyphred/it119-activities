import pandas as pd
import sys
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns


# Get input filename from args
filename = sys.argv[1]

# Read file into a data frame
df = pd.read_csv(filename)

df.isnull().values.any()
df.info()
df = df.rename(columns={"sleep(hrs)/weeknights":"sleepHrsWeeks"})
SlpSngle = df[(df['maritalStatus'] == "Single")].sleepHrsWeeks
SlpMarried = df[(df['maritalStatus'] == "Married")].sleepHrsWeeks
stats.anderson(SlpSngle, dist="norm")
stats.anderson(SlpMarried, dist="norm")

sns.set(style="whitegrid")
plt.figure(figsize=(10,8))
ax = sns.boxplot(x="maritalStatus", y="sleepHrsWeeks", data=df, orient="v")

plt.show()
