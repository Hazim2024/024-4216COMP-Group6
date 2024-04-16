import matplotlib.pyplot as plt
import pandas as pd

def hazim_visualisation():
    data = pd.read_csv("cbb.csv")
    averageOffensive = data.groupby(['YEAR', 'TEAM'])['ADJOE'].mean().unstack()
    top_5 = averageOffensive.mean().nlargest(5).index
    averageOffensiveTop_5 = averageOffensive[top_5]
    averageOffensiveTop_5.plot(kind='bar', width=0.8)
    plt.title('Average Offensive Efficiency of Top 5 Teams Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Average Offensive Efficiency (ADJOE)')
    plt.legend(title='Team', bbox_to_anchor=(1, 1))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def wissem_visualisation():
    data = pd.read_csv("cbb.csv")
    champion_teams = data[data['POSTSEASON'] == 'Champions']
    second_place_teams = data[data['POSTSEASON'] == '2ND']
    champion_avg_3P = champion_teams.groupby('YEAR')['3P_O'].mean().reset_index()
    second_place_avg_3P = second_place_teams.groupby('YEAR')['3P_O'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.barh(champion_avg_3P['YEAR'], champion_avg_3P['3P_O'], color='blue', label='Champion Teams')
    ax.barh(second_place_avg_3P['YEAR'], second_place_avg_3P['3P_O'], color='orange', label='Second Place Teams')
    ax.set_xlabel('Average Three-Pointer Shots')
    ax.set_ylabel('Year')
    ax.set_title('Average Three-Pointer Shots Comparison')
    ax.legend()
    plt.show()

def mavia_visualisation():
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

def jordy_visualisation():
    data = pd.read_csv("cbb.csv")
    average_winning_ratio = data.groupby('TEAM')['W'].mean()
    top_5_teams = average_winning_ratio.nlargest(5)
    plt.figure(figsize=(10, 6))
    plt.pie(top_5_teams, labels=top_5_teams.index, autopct='%1.1f%%', startangle=140)
    plt.title('Top 5 Teams with Highest Winning Ratio')
    plt.axis('equal')
    plt.show()

def aymane_visualisation():
    data = pd.read_csv("cbb.csv")
    champion_team_data = data[data['TEAM'] == "North Carolina"]
    performance_metrics = ['2P_D', '3P_D', 'ADJ_T', 'FTRD']
    years = champion_team_data['YEAR']
    plt.figure(figsize=(10, 6))
    for metric in performance_metrics:
        plt.plot(years, champion_team_data[metric], marker='o', label=metric, linestyle='-')
    plt.xlabel('Year')
    plt.ylabel('Performance')
    plt.title(f'Performance Trend of North Carolina Over the Years')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("Menu:")
        print("Press 1 for Aymane's Visualisation")
        print("Press 2 for Hazim's Visualisation")
        print("Press 3 for Mavia's Visualisation")
        print("Press 4 for Jordy's Visualisation")
        print("Press 5 for Wissem's Visualisation")
        print("Press 6 for Abdullah's Visualisation")
        print("Press 7 for Raghad's Visualisation")
        print("8. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            aymane_visiualisation()
        elif choice == '2':
            hazim_visiualisation()
        elif choice == '3':
            mavia_visiualisation()
        elif choice == '4':
            jordy_visiualisation()
        elif choice == '5':
            wissem_visiualisation()
        elif choice == '8':
            print("Thank you")
            break
        else:
            print("Please enter number from [1-8]")
main()
