import pandas as pd
from matplotlib import pyplot as plt

# Hypothesis: Higher extracurricular involvement correlates with higher employment rates across departments.

# Load data
df = pd.read_csv("ResearchInformation3.csv")

# User Interface for selecting Charts
print("1. Employment pie chart")
print("2. Extracurricular attendance pie chart")
print("3. Employment column chart")
print("4. Extracurricular attendance column chart")
print("5. Extracurricular activities vs Employment rate comparative column chart")
try:
    choice = int(input("Choose a chart: "))
    if choice not in range(1, 6):
        raise ValueError
except ValueError:
    print("Please enter a number between 1 and 5.")


if choice == 1:
    job_pie = df[df['Job'] != 'None']['Job'].value_counts()
    job_pie.plot(kind='pie', autopct='%1.1f%%', title='Employment')
    plt.ylabel('')  # Removes default y-axis label
    plt.tight_layout()
    plt.savefig("Employment_piechart.png")
    plt.show()
elif choice == 2:
    extra_pie = df[df['Extra'] != 'None']['Extra'].value_counts()
    extra_pie.plot(kind='pie', autopct='%1.1f%%', title='Extra-curricular attendance')
    plt.ylabel('')  
    plt.tight_layout()
    plt.savefig("Extracurricular_attendance_piechart.png")
    plt.show()
elif choice == 3:
    employment_col = df['Job'].value_counts().head(10)
    employment_col.plot(kind='bar', title='Employment rate')
    plt.xlabel('Job')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("employment_bar.png")
    plt.show()
elif choice == 4:
    extra_col = df['Extra'].value_counts().head(10)
    extra_col.plot(kind='bar', title='Extra-curricular attendance')
    plt.xlabel('Extracurricular')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("extra_bar.png")
    plt.show()
elif choice == 5:
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

