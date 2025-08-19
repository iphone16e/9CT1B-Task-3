from matplotlib import pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("ResearchInformation3.csv")

# Show the first 5 rows
print(df.head())

# Show the column names
print(df.columns)
medal_counts = df[df['Gender'] != 'None']['Gender'].value_counts()

medal_counts.plot(kind='pie', autopct='%1.1f%%', title='Gender')
plt.ylabel('')  # Removes default y-axis label
plt.tight_layout()
plt.savefig("Gender.png")
plt.show()