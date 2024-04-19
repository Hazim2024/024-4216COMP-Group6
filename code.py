import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("cbb.csv")
champion_teams = data[data['POSTSEASON'] == 'Champions']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
ax1.bar(champion_teams['TEAM'], champion_teams['2P_O'], color='orange', alpha=0.5)
ax1.set_title('Two-Pointers Shot for Champion Teams')
ax1.set_xlabel('Team')
ax1.set_ylabel('Two-Pointers Shot')
ax2.scatter(champion_teams['TEAM'], champion_teams['2P_D'], color='blue')
ax2.set_title('Two-Pointers Allowed for Champion Teams')
ax2.set_xlabel('Team')
ax2.set_ylabel('Two-Pointers Allowed')
plt.tight_layout()
plt.show()