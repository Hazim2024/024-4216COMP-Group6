import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("cbb.csv")

#Calculate average offensive efficiency for every team for each year
averageOffensive = data.groupby(['YEAR', 'TEAM'])['ADJOE'].mean().unstack()
# Get the top 5 teams with the highest average
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


# Average Three Pointer Comparision between 2nd and Champion Teams
champion_teams = data[data['POSTSEASON'] == 'Champions']
second_place_teams = data[data['POSTSEASON'] == '2ND']
# calculate the average three-pointer shots for champion teams
chamAvg3P = champion_teams.groupby('YEAR')['3P_O'].mean().reset_index()
# Calculate the average three-pointer shots for second-place teams
secondPlace3P = second_place_teams.groupby('YEAR')['3P_O'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(chamAvg3P['YEAR'], chamAvg3P['3P_O'], color='blue', label='Champion Teams')
ax.barh(secondPlace3P['YEAR'], secondPlace3P['3P_O'], color='orange', label='Second Place Teams')
ax.set_xlabel('Average Three-Pointer Shots')
ax.set_ylabel('Year')
ax.set_title('Average Three-Pointer Shots Comparison')
ax.legend()
plt.show()
