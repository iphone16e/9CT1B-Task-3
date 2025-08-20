import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("ResearchInformation3.csv")

# Replace these with actual column names from your dataset
group_col = 'Department'       # Grouping variable
extra_col = 'Extra'             # Extracurricular participation
job_col = 'Job'                 # Employment status

# Clean and group data
df_clean = df[[group_col, extra_col, job_col]].dropna()

# Calculate participation and employment rates per group
summary = df_clean.groupby(group_col).agg({
    extra_col: lambda x: (x == 'Yes').mean() * 100,
    job_col: lambda x: (x == 'Yes').mean() * 100
}).rename(columns={extra_col: 'Extracurricular Rate', job_col: 'Employment Rate'})

# Plot
summary.plot(kind='bar', figsize=(12, 6))
plt.title('Extracurricular Participation vs Employment Rate by Department')
plt.ylabel('Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("extracurricular_vs_employment.png")
plt.show()
