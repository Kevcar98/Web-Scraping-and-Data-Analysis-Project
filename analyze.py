import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the csv file
df = pd.read_csv('books.csv')

# Converts price to numeric value
df['Price'] = df['Price'].str.replace('£', '').astype(float)

# Basic Analysis
print('Basic Analysis')
print('Number of Books:', df.shape[0])
print('Average Price:', df['Price'].mean(), '\n')
print("Basic Statistics:")
print(df.describe(), '\n')

# Plotting
print('Plotting')

plt.hist(df['Price'], bins=20, color='skyblue', edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')

# Save the plot as a png file
plt.savefig('price_distribution.png')

# Show the plot
plt.show()

# Plotting price distribution by rating
plt.figure(figsize=(10, 6))
sns.boxplot(x='Star Rating', y='Price', data=df)
plt.title('Price Distribution by Rating')
plt.xlabel('Rating')
plt.ylabel('Price')

# Save the plot as a png file
plt.savefig('price_distribution_by_rating.png')

# Show the plot
plt.show()

# Save the DataFrame to a csv file
df.to_csv('books_cleaned.csv', index=False)
