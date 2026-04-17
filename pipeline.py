import pandas as pd

# Load data
df = pd.read_csv("sales.csv")

print("Original Data:")
print(df)

# Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Transformation
total_sales = df["sales"].sum()
top_product = df.groupby("product")["sales"].sum().idxmax()

print("\nTotal Sales:", total_sales)
print("Top Product:", top_product)

# Save cleaned data
df.to_csv("cleaned_sales.csv", index=False)

print("\nCleaned data saved successfully!")