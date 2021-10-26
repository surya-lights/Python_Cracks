import pandas as pd
import sys
import matplotlib.pyplot as plt


df = pd.read_csv('test_file.csv')

print(df.to_string(index=False))

df.plot()

plt.show()


plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
