import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a random list of values
data = [3, 1, 0, 0, 0, 0, 2, 2, 5, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 12, 4, 3, 1, 0, 0, 11, 4, 8, 18, 3, 5, 5, 14, 6, 0, 0, 0, 0, 9, 0, 12, 17, 4, 0, 0, 0, 13, 12, 14, 3, 3, 0, 0, 5, 12, 0, 8, 0, 0, 0, 2, 7, 15, 28, 0, 0, 12, 10, 0, 18, 16, 16, 0, 0, 12, 1, 8, 7, 0, 0, 16, 8, 14, 18, 17, 16, 0, 3, 10, 0, 9, 0, 0, 0, 0, 8, 0, 9, 1, 13, 3, 1, 0, 0, 0, 0, 0, 9, 0, 2, 7, 9, 18, 0, 28, 0, 0, 12, 23, 16, 17, 2, 22, 15, 0, 10, 41, 0, 18, 6, 8, 10, 17, 3, 1, 0, 13, 12, 1, 5, 10, 5, 14, 3, 4, 12, 12, 4, 7, 9, 10, 13, 45, 2, 3, 3, 12, 7, 14, 35, 12, 31, 15, 5, 11, 51, 9, 34, 38, 17, 20, 7, 5, 43, 32, 22, 0, 3, 19, 27, 25, 29, 42, 16, 35, 3, 36, 23, 1, 9, 18, 0, 2, 39, 40, 41, 1, 5, 4, 2, 23, 1, 6, 6, 1, 0, 17, 16, 5, 14, 10, 6, 12, 14, 2, 3, 2, 0, 24, 2, 28, 18, 0, 12, 27, 2, 0, 15, 9, 0, 0, 11, 8, 6, 15, 27, 4, 3, 5, 10, 6, 8, 21, 7, 22, 10, 0, 2, 4, 9, 17, 10, 11, 5, 0, 21, 29, 1, 24, 25, 15, 36, 28, 7, 7, 1, 0, 0, 0, 3, 4, 3, 21, 3, 11, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13, 5, 0, 7, 23, 0, 2, 2, 6, 0, 1, 0, 1, 14, 11, 15, 2, 0, 4, 11, 3, 12, 0, 0, 0, 4, 0, 3, 11, 1, 2, 0, 32, 5, 0, 0, 8, 17, 5, 1, 0, 1, 1, 3, 1, 0, 5, 0, 6, 0, 4, 0, 0, 0, 10, 12, 4, 0, 7, 0, 0, 0, 12]

# In our heatmap, nan will mean "no such date", e.g. 31 June
pivoted_data = np.array(data).reshape(52, 7)
pivoted_data = np.transpose(pivoted_data)
print(pivoted_data)
cmap = plt.cm.get_cmap('YlOrRd')
plt.figure(figsize = (16, 6))
sns.heatmap(pivoted_data, linewidths=5, cmap=cmap,linecolor='white', square=True, cbar=False, edgecolor='white')

plt.savefig('heatmap.png')