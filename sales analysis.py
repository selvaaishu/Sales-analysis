import pandas as pd

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Basic information
print("\nShape of dataset (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

# Check missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Handle missing values
df.fillna(0, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Calculate metrics
total_revenue = df["Total Sales"].sum()
average_sales = df["Total Sales"].mean()
highest_sale = df["Total Sales"].max()
lowest_sale = df["Total Sales"].min()

best_selling_product = df.groupby("Product")["Total Sales"].sum().idxmax()
sales_by_region = df.groupby("Region")["Total Sales"].sum()

# Print report
print("\n========== SALES REPORT ==========")
print("Total Revenue:", total_revenue)
print("Average Sales:", round(average_sales, 2))
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Best Selling Product:", best_selling_product)

print("\nSales by Region:")
print(sales_by_region)

print("\nAnalysis completed successfully ✅")
