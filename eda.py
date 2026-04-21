import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("train.csv")

# Create figure with multiple charts in one sheet
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Superstore Sales Dashboard", fontsize=16)

# 1. Sales by Region
df.groupby("Region")["Sales"].sum().plot(kind="bar", ax=axes[0,0])
axes[0,0].set_title("Sales by Region")
axes[0,0].set_xlabel("Region")
axes[0,0].set_ylabel("Sales")

# 2. Sales by Category
df.groupby("Category")["Sales"].sum().plot(kind="bar", ax=axes[0,1])
axes[0,1].set_title("Sales by Category")
axes[0,1].set_xlabel("Category")
axes[0,1].set_ylabel("Sales")

# 3. Top 10 States by Sales
df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10).plot(kind="bar", ax=axes[1,0])
axes[1,0].set_title("Top 10 States by Sales")
axes[1,0].set_xlabel("State")
axes[1,0].set_ylabel("Sales")

# 4. Sales Distribution Histogram
df["Sales"].plot(kind="hist", bins=30, ax=axes[1,1])
axes[1,1].set_title("Sales Distribution")
axes[1,1].set_xlabel("Sales")

plt.tight_layout()
plt.show()