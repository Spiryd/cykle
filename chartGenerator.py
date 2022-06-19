import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#ds1 = pd.read_csv('test.csv', sep=";")
ds2 = pd.read_csv('zadanie.csv', sep=";")
#ds3 = pd.read_csv('harmonic.csv', sep=";")
#ds1.columns = ["n", "avrage number of cycles"]
ds2.columns = ["n", "avrage max length of a cycle in a permutation"]
#ds3.columns = ["n", "harmonic num"]
#g1 = sns.relplot(x="n", y="avrage number of cycles",kind="line"  ,data = ds1)
g2 = sns.relplot(x="n", y="avrage max length of a cycle in a permutation",kind="line", data = ds2)
#g3 = sns.scatterplot(x="n", y="harmonic num", data = ds3)
plt.show(block=True)