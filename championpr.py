import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the data from the "cbb.csv" dataset .
data = pd.read_csv("cbb.csv")

# Filter the data for years from 2013 to 2023 no data for 2020 because of covid
data_filtered = data[(data['YEAR'] >= 2013) & (data['YEAR'] <= 2023)]

# Initialize lists to store average power ratings for champions and runners-up
champion_ratings = []
runner_up_ratings = []

# Iterate over each year from 2013 to 2023
for year in range(2013, 2024):
    # Filter the data for the current year and separate champions and runners-up
    year_data = data_filtered[data_filtered['YEAR'] == year]
    champion_data = year_data[year_data['POSTSEASON'] == 'Champions']
    runner_up_data = year_data[year_data['POSTSEASON'] == '2ND']
    
    # Calculate the average power ratings for champions and runners-up
    champion_rating = champion_data['BARTHAG'].mean()
    runner_up_rating = runner_up_data['BARTHAG'].mean()
    
    # Append the average ratings to the lists
    champion_ratings.append(champion_rating)
    runner_up_ratings.append(runner_up_rating)

# Plot the comparison on a bar graph with different colors for champions and runners-up
bar_width = 0.4
index = np.arange(len(champion_ratings))

plt.bar(index, champion_ratings, width=bar_width, color='blue', label='Champion')
plt.bar(index + bar_width, runner_up_ratings, width=bar_width, color='red', label='Runner-Up', alpha=0.7)
plt.title('Average Power Ratings Comparison of Champions and Runners-Up (2013-2023)')
plt.xlabel('Year')
plt.ylabel('Average Power Rating')
plt.xticks(index + bar_width / 2, range(2013, 2024))
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
