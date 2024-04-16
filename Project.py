import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("cbb.csv")
#Calculate average offensive efficiency for every team for each year
averageOffensive = data.groupby(['YEAR', 'TEAM'])['ADJOE'].mean().unstack()
# Get the top 5 teams with the highest Average Offensive Efficiency (ADJOE)
top_5 = averageOffensive.mean().nlargest(5).index
#Filter the data to include only the top 5 teams
averageOffensiveTop_5 = averageOffensive[top_5]
#Plot the bar graph
averageOffensiveTop_5.plot(kind='bar', width=0.8)
plt.title('Average Offensive Efficiency of Top 5 Teams Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Offensive Efficiency (ADJOE)')
plt.legend(title='Team', bbox_to_anchor=(1, 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
