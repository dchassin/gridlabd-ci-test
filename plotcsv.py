import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("my_test.csv",header=None,names=["Indoor"])
plt.figure(1)
data[-24*60:].plot()
plt.xlabel("Date/Time")
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.5)
plt.grid()
plt.ylabel("Air temperature [degF]")
plt.savefig("my_test.png")
