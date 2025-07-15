import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Show basic info
print("First 5 rows of the dataset:")
print(df.head())

print("\nMissing values per column:")
print(df.isnull().sum())

# Top 5 genres
print("\nTop genres:")
print(df['genre'].value_counts().head())

# Content count by country (Top 5)
print("\nContent count by country:")
print(df['country'].value_counts().head())

# Movies vs TV Shows (based on duration format)
df['type'] = df['duration'].apply(lambda x: 'TV Show' if 'Season' in str(x) else 'Movie')
type_counts = df['type'].value_counts()

# Pie chart for content type
plt.figure(figsize=(6, 6))
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'])
plt.title("Distribution of Movies vs TV Shows on Netflix")
plt.savefig("content_type_pie.png")
plt.show()

# Releases over the years
year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
sns.lineplot(x=year_counts.index, y=year_counts.values, marker='o')
plt.title("Netflix Content Release Trend Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Releases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("release_trend.png")
plt.show()
