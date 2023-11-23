import numpy as np
import pandas as pd
from scipy.stats import bartlett
import matplotlib.pyplot as plt
import seaborn as sns
# Read data from CSV
data = pd.read_csv('example_data.csv')
# Perform Bartlett's test
statistic, p_value = bartlett(data['Group1'], data['Group2'])
# Display the results
print(f'Bartlett Statistic: {statistic}')
print(f'P-value: {p_value}')
# Set seaborn style for better aesthetics
sns.set(style="whitegrid")
# Visualize the data with boxplot, swarm plot, and violin plot
plt.figure(figsize=(12, 8))
boxplot = sns.boxplot(data=data, palette="Pastel1", width=0.5)
swarmplot = sns.swarmplot(data=data, color=".25", size=6, alpha=0.7)
violinplot = sns.violinplot(data=data, palette="Pastel2", inner="quartile")
# Add markers for average and median values
for i, group_name in enumerate(data.columns):
    average = np.mean(data[group_name])
    median = np.median(data[group_name])
    # Mark average with a red dot
    boxplot.plot(i, average, marker='o', markersize=8, color='red', label=f'Average {group_name}')
    # Mark median with a green dot
    boxplot.plot(i, median, marker='o', markersize=8, color='green', label=f'Median {group_name}')
    # Display numeric values above the dots with arrows
    plt.annotate(f'{average:.2f}', xy=(i, average), xytext=(i, average + 2),
                 arrowprops=dict(facecolor='red', arrowstyle='->', color="red"), color='red', ha='left')
    plt.annotate(f'{median:.2f}', xy=(i, median), xytext=(i, median - 2),
                 arrowprops=dict(facecolor='green', arrowstyle='->',color="green"), color='green', ha='right')
# Adjust legend position
boxplot.legend(loc='upper left')
plt.title('Bartletts test: Boxplot, swarm plot, violin plot and average, and median values')
plt.ylabel('Values')
plt.xlabel('Groups')
plt.show()
