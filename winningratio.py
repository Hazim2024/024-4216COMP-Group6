import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the "cbb.csv" dataset
data = pd.read_csv("cbb.csv")

# Calculate the winning ratio for each team
data['Winning Ratio'] = data['W'] / data['G']

# Initialize an empty list to store the top 5 conferences for each year
top_conferences_by_year = []

# Iterate over the years
for year in range(2013, 2024):
    # Filter the data for the current year
    year_data = data[data['YEAR'] == year]
    
    # Group the data by conference and calculate the mean winning ratio for each conference
    conference_stats = year_data.groupby('CONF').agg({'Winning Ratio': 'mean', 'TEAM': 'count'}).reset_index()
    conference_stats.rename(columns={'TEAM': 'Total Teams'}, inplace=True)
    
    # Sort the conferences by their average winning ratio and total number of teams
    conference_stats.sort_values(by=['Winning Ratio', 'Total Teams'], ascending=[False, False], inplace=True)
    
    # Get the top 5 conferences for the current year
    top_5_conferences = conference_stats.head(5)
    
    # Store the top 5 conferences for the current year in the list
    top_conferences_by_year.append(top_5_conferences)

# Extract top 5 conference names and winning ratios for each year
conference_names = []
winning_ratios = []

for year_conferences in top_conferences_by_year:
    conference_names.extend(year_conferences['CONF'])
    winning_ratios.extend(year_conferences['Winning Ratio'])

# Get unique conference names and years
unique_conferences = sorted(set(conference_names))
years = range(2013, 2024)

# Create a dictionary to store winning ratios for each conference and year
data_dict = {conference: [] for conference in unique_conferences}
for year_conferences in top_conferences_by_year:
    for conference in unique_conferences:
        if conference in year_conferences['CONF'].values:
            data_dict[conference].append(year_conferences.loc[year_conferences['CONF'] == conference, 'Winning Ratio'].values[0])
        else:
            data_dict[conference].append(0)

# Plot grouped bar chart
plt.figure(figsize=(12, 8))
bar_width = 0.15
index = range(len(years))

for i, conference in enumerate(unique_conferences):
    plt.bar([x + i * bar_width for x in index], data_dict[conference], bar_width, label=conference)

# Add labels to the bars
for i, conference in enumerate(unique_conferences):
    for j, year in enumerate(years):
        plt.text(year + (i + 0.5) * bar_width, data_dict[conference][j], conference,
                 ha='center', va='bottom', rotation=90, fontsize=8)

plt.xlabel('Year')
plt.ylabel('Weighted Average Winning Ratio')
plt.title('Top 5 Conferences with Highest Winning Ratios (2013-2023)')
plt.xticks([x + 2 * bar_width for x in index], years, rotation=45, ha='right')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


