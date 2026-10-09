import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# 1. CREATE OUTPUT FOLDER
# ==========================================

os.makedirs("charts", exist_ok=True)
os.makedirs("reports", exist_ok=True)


# ==========================================
# 2. LOAD CLEANED DATASET
# ==========================================

file_path = "data/titanic_cleaned.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")


# ==========================================
# 3. BASIC DATA INFORMATION
# ==========================================

print("\n========== DATASET INFORMATION ==========")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)


# ==========================================
# 4. STATISTICAL SUMMARY
# ==========================================

print("\n========== STATISTICAL SUMMARY ==========")

print(df.describe())

# Save statistical summary
df.describe().to_csv(
    "reports/statistical_summary.csv"
)


# ==========================================
# 5. MISSING VALUES
# ==========================================

print("\n========== MISSING VALUES ==========")

print(df.isnull().sum())


# ==========================================
# 6. SURVIVAL COUNT
# ==========================================

print("\n========== SURVIVAL ANALYSIS ==========")

print(df["survived"].value_counts())

survival_rate = df["survived"].mean() * 100

print(
    f"\nOverall survival rate: "
    f"{survival_rate:.2f}%"
)


# ==========================================
# 7. SURVIVAL BY GENDER
# ==========================================

print("\n========== SURVIVAL BY GENDER ==========")

gender_survival = (
    df.groupby("sex")["survived"]
    .mean() * 100
)

print(gender_survival)


# ==========================================
# 8. SURVIVAL BY PASSENGER CLASS
# ==========================================

print("\n========== SURVIVAL BY CLASS ==========")

class_survival = (
    df.groupby("pclass")["survived"]
    .mean() * 100
)

print(class_survival)


# ==========================================
# 9. AVERAGE AGE BY SURVIVAL
# ==========================================

print("\n========== AGE ANALYSIS ==========")

age_survival = df.groupby("survived")["age"].mean()

print(age_survival)


# ==========================================
# 10. AVERAGE FARE BY CLASS
# ==========================================

print("\n========== FARE ANALYSIS ==========")

fare_class = df.groupby("pclass")["fare"].mean()

print(fare_class)


# ==========================================
# 11. PASSENGERS BY EMBARKED LOCATION
# ==========================================

print("\n========== EMBARKATION ANALYSIS ==========")

print(df["embarked"].value_counts())


# ==========================================
# 12. CHART 1 - SURVIVAL COUNT
# ==========================================

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="survived"
)

plt.title("Passenger Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")

plt.tight_layout()

plt.savefig(
    "charts/01_survival_count.png"
)

plt.show()


# ==========================================
# 13. CHART 2 - SURVIVAL BY GENDER
# ==========================================

plt.figure(figsize=(7, 5))

sns.barplot(
    data=df,
    x="sex",
    y="survived"
)

plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")

plt.tight_layout()

plt.savefig(
    "charts/02_survival_by_gender.png"
)

plt.show()


# ==========================================
# 14. CHART 3 - SURVIVAL BY CLASS
# ==========================================

plt.figure(figsize=(7, 5))

sns.barplot(
    data=df,
    x="pclass",
    y="survived"
)

plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")

plt.tight_layout()

plt.savefig(
    "charts/03_survival_by_class.png"
)

plt.show()


# ==========================================
# 15. CHART 4 - AGE DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="age",
    bins=30,
    kde=True
)

plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.tight_layout()

plt.savefig(
    "charts/04_age_distribution.png"
)

plt.show()


# ==========================================
# 16. CHART 5 - FARE DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="fare",
    bins=30,
    kde=True
)

plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")

plt.tight_layout()

plt.savefig(
    "charts/05_fare_distribution.png"
)

plt.show()


# ==========================================
# 17. CHART 6 - CLASS DISTRIBUTION
# ==========================================

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="pclass"
)

plt.title("Passenger Distribution by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")

plt.tight_layout()

plt.savefig(
    "charts/06_class_distribution.png"
)

plt.show()


# ==========================================
# 18. CHART 7 - SURVIVAL BY GENDER AND CLASS
# ==========================================

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="pclass",
    y="survived",
    hue="sex"
)

plt.title("Survival Rate by Class and Gender")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")

plt.tight_layout()

plt.savefig(
    "charts/07_class_gender_survival.png"
)

plt.show()


# ==========================================
# 19. CORRELATION ANALYSIS
# ==========================================

numeric_df = df.select_dtypes(
    include="number"
)

correlation = numeric_df.corr()

print("\n========== CORRELATION MATRIX ==========")

print(correlation)


# ==========================================
# 20. CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(9, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    "charts/08_correlation_heatmap.png"
)

plt.show()


# ==========================================
# 21. FIND HIGHEST AND LOWEST FARE
# ==========================================

highest_fare = df["fare"].max()
lowest_fare = df["fare"].min()

print("\nHighest fare:", highest_fare)
print("Lowest fare:", lowest_fare)


# ==========================================
# 22. CREATE EDA REPORT
# ==========================================

with open(
    "reports/eda_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write(
        "SWYNEX TASK 2 - EXPLORATORY DATA ANALYSIS\n"
    )

    report.write("=" * 55 + "\n\n")

    report.write("Dataset: Titanic Dataset\n\n")

    report.write("DATASET OVERVIEW\n")
    report.write("-" * 30 + "\n")

    report.write(
        f"Rows: {df.shape[0]}\n"
    )

    report.write(
        f"Columns: {df.shape[1]}\n\n"
    )

    report.write("IMPORTANT STATISTICS\n")
    report.write("-" * 30 + "\n")

    report.write(
        str(df.describe())
    )

    report.write("\n\nSURVIVAL RATE\n")
    report.write("-" * 30 + "\n")

    report.write(
        f"Overall survival rate: "
        f"{survival_rate:.2f}%\n"
    )

    report.write("\nSURVIVAL BY GENDER\n")
    report.write("-" * 30 + "\n")

    report.write(
        str(gender_survival)
    )

    report.write("\n\nSURVIVAL BY CLASS\n")
    report.write("-" * 30 + "\n")

    report.write(
        str(class_survival)
    )

    report.write("\n\nAVERAGE AGE BY SURVIVAL\n")
    report.write("-" * 30 + "\n")

    report.write(
        str(age_survival)
    )

    report.write("\n\nAVERAGE FARE BY CLASS\n")
    report.write("-" * 30 + "\n")

    report.write(
        str(fare_class)
    )

    report.write("\n\nPASSENGERS BY EMBARKATION\n")
    report.write("-" * 30 + "\n")

    report.write(
        str(df["embarked"].value_counts())
    )


# ==========================================
# 23. FINISH
# ==========================================

print("\n========================================")
print("EDA COMPLETED SUCCESSFULLY!")
print("========================================")

print("\nCharts saved inside:")
print("charts/")

print("\nReports saved inside:")
print("reports/")