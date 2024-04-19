import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("cbb.csv")

average_offensive_efficiency = data.groupby(['YEAR', 'TEAM'])['ADJOE'].mean().unstack()

top_5_teams = average_offensive_efficiency.mean().nlargest(5).index

average_offensive_efficiency_top_5 = average_offensive_efficiency[top_5_teams]

plt.figure(figsize=(12, 8))
average_offensive_efficiency_top_5.plot(kind='bar', width=0.8)
plt.title('Average Offensive Efficiency of Top 5 Teams Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Offensive Efficiency (ADJOE)') 
plt.legend(title='Team', bbox_to_anchor=(1, 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()