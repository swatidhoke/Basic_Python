"""
PANDAS CHEAT SHEET – BEGINNER FRIENDLY
------------------------------------
Pandas is used for working with tabular data (rows & columns),
similar to Excel or SQL tables.

Key objects:
- Series  → 1D (single column)
- DataFrame → 2D (rows + columns)
"""
import pandas as pd

# --------------------------------------------------
# 1️⃣ Creating Data
# --------------------------------------------------

# From a dictionary (most common)
# Keys = column names
# Values = list of values (must be same length)
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["NY", "SF", "LA"]
}

df = pd.DataFrame(data)
print("DataFrame from dictionary:\n", df)

# --------------------------------------------------
# 2️⃣ Reading Data
# --------------------------------------------------

# CSV file
# df = pd.read_csv("data.csv")

# Excel file
# df = pd.read_excel("data.xlsx")

# df = pd.read_sql("SELECT * FROM users", engine)
# print(df.head())

# --------------------------------------------------
# 3️⃣ Inspecting Data
# --------------------------------------------------

print("\nFirst 2 rows:\n", df.head(2))     # default = 5
print("\nLast 2 rows:\n", df.tail(2))

print("\nShape (rows, columns):", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData types:\n", df.dtypes)

print("\nSummary statistics:\n", df.describe())

# --------------------------------------------------
# 4️⃣ Selecting Data
# --------------------------------------------------

# Select a single column (returns Series – 1D)
ages = df["age"]
print("\nAge column:\n", ages)

# Select multiple columns (returns DataFrame – 2D)
subset = df[["name", "city"]]
print("\nName & City:\n", subset)

# Select rows by index position
print("\nFirst row using iloc:\n", df.iloc[0])

# Select rows by condition
adults = df[df["age"] > 28]
print("\nPeople older than 28:\n", adults)

# --------------------------------------------------
# 5️⃣ Sorting
# --------------------------------------------------

# Sort by one column
sorted_by_age = df.sort_values(by="age")
print("\nSorted by age:\n", sorted_by_age)

# Sort descending
sorted_desc = df.sort_values(by="age", ascending=False)
print("\nSorted by age (desc):\n", sorted_desc)

# --------------------------------------------------
# 6️⃣ Adding / Modifying Columns
# --------------------------------------------------

# Create a new column
df["age_plus_10"] = df["age"] + 10
print("\nNew column added:\n", df)

# --------------------------------------------------
# 7️⃣ Dropping Data
# --------------------------------------------------

# Drop a column
df_no_city = df.drop(columns=["city"])
print("\nDropped city column:\n", df_no_city)

# Drop a row by index
df_no_row = df.drop(index=0)
print("\nDropped first row:\n", df_no_row)

# --------------------------------------------------
# 8️⃣ Handling Missing Values
# --------------------------------------------------

# Create sample data with missing value
data_missing = {
    "name": ["A", "B", "C"],
    "score": [90, None, 85]
}

df_missing = pd.DataFrame(data_missing)

print("\nWith missing values:\n", df_missing)

# Fill missing values
df_filled = df_missing.fillna(0)
print("\nFilled missing values:\n", df_filled)

# Drop rows with missing values
df_dropped = df_missing.dropna()
print("\nDropped missing rows:\n", df_dropped)

# --------------------------------------------------
# 9️⃣ Group By (Very Important)
# --------------------------------------------------

sales = {
    "city": ["NY", "NY", "SF", "SF"],
    "revenue": [100, 200, 150, 300]
}

sales_df = pd.DataFrame(sales)

grouped = sales_df.groupby("city")["revenue"].sum()
print("\nRevenue by city:\n", grouped)

# --------------------------------------------------
# 🔟 Exporting Data
# --------------------------------------------------

# Save to CSV
# df.to_csv("output.csv", index=False)

# Save to Excel
# df.to_excel("output.xlsx", index=False)

# --------------------------------------------------
# ✅ QUICK REFERENCE
# --------------------------------------------------
"""
df.head(n)            → first n rows
df.tail(n)            → last n rows
df.shape              → (rows, columns)
df.columns            → column names
df['col']             → select column
df[df['col'] > x]     → filter rows
df.sort_values()      → sort
df.groupby()          → aggregate
df.fillna()           → handle missing values
"""

print("\n--- End of Pandas Cheat Sheet ---")
