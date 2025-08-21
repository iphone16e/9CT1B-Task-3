import pandas as pd
from matplotlib import pyplot as plt

# Hypothesis: Higher extracurricular involvement correlates with higher employment rates across departments.

# Load data
df = pd.read_csv("ResearchInformation3.csv")

# Filter out rows with missing or 'None' values in key columns
df = df[(df['Department'].notna()) & (df['Extra'] != 'None') & (df['Job'] != 'None')]

# Helper function to display data tables
def show_table(df_table, title):
    print(f"\n--- {title} ---")
    print(df_table.to_string())

while True:
    # User Interface for selecting Charts
    print("\nChart Options:")
    print("1. Employment pie chart")
    print("2. Extracurricular attendance pie chart")
    print("3. Employment column chart")
    print("4. Extracurricular attendance column chart")
    print("5. Extracurricular activities vs Employment rate comparative column chart")
    print("6. View data tables only")
    print("0. Exit")

    try:
        choice = int(input("Choose an option (0 to exit): "))
        if choice == 0:
            print("Exiting program.")
            break
        if choice not in range(1, 7):
            raise ValueError
    except ValueError:
        print("Please enter a number between 0 and 6.")
        continue

    if choice == 1:
        job_pie = df['Job'].value_counts()
        job_pie.plot(kind='pie', autopct='%1.1f%%', title='Employment')
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig("Employment_piechart.png")
        plt.show()
        input("Press Enter to continue...")
        if input("Show data table? (y/n): ").lower() == 'y':
            show_table(job_pie, "Employment Data")

    elif choice == 2:
        extra_pie = df['Extra'].value_counts()
        extra_pie.plot(kind='pie', autopct='%1.1f%%', title='Extra-curricular attendance')
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig("Extracurricular_attendance_piechart.png")
        plt.show()
        input("Press Enter to continue...")
        if input("Show data table? (y/n): ").lower() == 'y':
            show_table(extra_pie, "Extracurricular Attendance Data")

    elif choice == 3:
        employment_col = df['Job'].value_counts().head(10)
        employment_col.plot(kind='bar', title='Employment rate')
        plt.xlabel('Job')
        plt.ylabel('Rate')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("employment_bar.png")
        plt.show()
        input("Press Enter to continue...")
        if input("Show data table? (y/n): ").lower() == 'y':
            show_table(employment_col, "Top 10 Employment Categories")

    elif choice == 4:
        extra_col = df['Extra'].value_counts().head(10)
        extra_col.plot(kind='bar', title='Extra-curricular attendance')
        plt.xlabel('Extracurricular')
        plt.ylabel('Rate')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("extra_bar.png")
        plt.show()
        input("Press Enter to continue...")
        if input("Show data table? (y/n): ").lower() == 'y':
            show_table(extra_col, "Top 10 Extracurricular Activities")

    elif choice == 5:
        group_col = 'Department'
        extra_col = 'Extra'
        job_col = 'Job'
        df_clean = df[[group_col, extra_col, job_col]].dropna()
        summary = df_clean.groupby(group_col).agg({
            extra_col: lambda x: (x == 'Yes').mean() * 100,
            job_col: lambda x: (x == 'Yes').mean() * 100
        }).rename(columns={extra_col: 'Extracurricular Rate', job_col: 'Employment Rate'})
        summary.plot(kind='bar', figsize=(12, 6))
        plt.title('Extracurricular Participation vs Employment Rate by Department')
        plt.ylabel('Rate (%)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("extracurricular_vs_employment.png")
        plt.show()
        input("Press Enter to continue...")
        if input("Show data table? (y/n): ").lower() == 'y':
            show_table(summary, "Departmental Comparison")

    elif choice == 6:
        print("\nData Table Options:")
        print("1. Employment Data")
        print("2. Extracurricular Attendance Data")
        print("3. Top 10 Employment Categories")
        print("4. Top 10 Extracurricular Activities")
        print("5. Departmental Comparison")
        try:
            table_choice = int(input("Choose a table to view: "))
            if table_choice == 1:
                show_table(df['Job'].value_counts(), "Employment Data")
            elif table_choice == 2:
                show_table(df['Extra'].value_counts(), "Extracurricular Attendance Data")
            elif table_choice == 3:
                show_table(df['Job'].value_counts().head(10), "Top 10 Employment Categories")
            elif table_choice == 4:
                show_table(df['Extra'].value_counts().head(10), "Top 10 Extracurricular Activities")
            elif table_choice == 5:
                group_col = 'Department'
                extra_col = 'Extra'
                job_col = 'Job'
                df_clean = df[[group_col, extra_col, job_col]].dropna()
                summary = df_clean.groupby(group_col).agg({
                    extra_col: lambda x: (x == 'Yes').mean() * 100,
                    job_col: lambda x: (x == 'Yes').mean() * 100
                }).rename(columns={extra_col: 'Extracurricular Rate', job_col: 'Employment Rate'})
                show_table(summary, "Departmental Comparison")
            else:
                print("Invalid table choice.")
        except ValueError:
            print("Please enter a valid number.")
