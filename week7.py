"""
Analyzing Data with Pandas and Visualizing Results with Matplotlib
Assignment Script
"""

import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# Task 1: Load and Explore Dataset
# ===============================

# load your kaggle dataset
df = pd.read_csv("iris.csv")

print("=== First 5 Rows ===")
print(df.head())

print("\n=== Dataset Info ===")
print(df.info())

print("\n=== Missing Values ===")
print(df.isnull().sum())

# Drop missing values (if any)
df = df.dropna()

# ===============================
# Task 2: Basic Data Analysis
# ===============================

print("\n=== Statistical Summary ===")
print(df.describe())

# Example: Group by species and compute mean petal length
if "species" in df.columns:
    grouped = df.groupby("species")["petal_length"].mean()
    print("\n=== Mean Petal Length per Species ===")
    print(grouped)

# ===============================
# Task 3: Data Visualization
# ===============================

plt.style.use("seaborn-v0_8")  # optional for clean visuals

# 1. Line Chart (trend of sepal length across index)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal_length"], label="Sepal Length", color="blue")
plt.title("Sepal Length Trend Over Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.legend()
plt.savefig("line_chart.png")
plt.close()

# 2. Bar Chart (average petal length per species)
if "species" in df.columns:
    plt.figure(figsize=(8, 5))
    grouped.plot(kind="bar", color="orange")
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Avg Petal Length")
    plt.tight_layout()
    plt.savefig("bar_chart.png")
    plt.close()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8, 5))
plt.hist(df["sepal_width"], bins=15, color="green", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.close()

# 4. Scatter Plot (sepal length vs petal length)
plt.figure(figsize=(8, 5))
plt.scatter(df["sepal_length"], df["petal_length"], alpha=0.7, c="red")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.savefig("scatter_plot.png")
plt.close()

# ===============================
# Findings/Observations
# ===============================

print("\n=== Observations ===")
print("- Sepal length values show steady variation across samples.")
print("- Average petal length differs clearly between species (Setosa smallest).")
print("- Sepal width distribution is close to normal.")
print("- Sepal length and petal length show strong positive correlation.")

print("\nCharts saved as: line_chart.png, bar_chart.png, histogram.png, scatter_plot.png")
