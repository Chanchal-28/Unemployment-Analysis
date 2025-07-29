# analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment in India.csv")
print("Initial Data:\n", df.head())

# Rename columns for easier use
df.columns = ['Region', 'Date', 'Frequency', 'Estimated Unemployment Rate (%)',
              'Estimated Employed', 'Estimated Labour Participation Rate (%)',
              'Area']

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# ------------------- Visualization 1: Unemployment Trend Over Time -------------------
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)', hue='Region')
plt.title('Unemployment Rate Over Time by Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------- Visualization 2: State-wise Average Unemployment -------------------
plt.figure(figsize=(10,6))
state_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values()
state_avg.plot(kind='barh', color='skyblue')
plt.title("Average Unemployment Rate by State")
plt.xlabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ------------------- Visualization 3: Heatmap -------------------
pivot = df.pivot_table(values='Estimated Unemployment Rate (%)',
                       index=df['Date'].dt.month, columns='Region')
plt.figure(figsize=(14,7))
sns.heatmap(pivot, cmap="YlGnBu", linewidths=0.5)
plt.title("Monthly Unemployment Rate Heatmap by Region")
plt.tight_layout()
plt.show()
