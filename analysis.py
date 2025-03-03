import pandas as pd
import sqlalchemy
import psycopg2
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt
import seaborn as sns

#Load CSV files
products_df = pd.read_csv("PRODUCTS_TAKEHOME.csv")
transactions_df = pd.read_csv("TRANSACTION_TAKEHOME.csv")
users_df = pd.read_csv("USER_TAKEHOME.csv")

#Display dataset info
print("Products Table Info:")
print(products_df.info())

print("Transactions Table Info:")
print(transactions_df.info())

print(" Users Table Info:")
print(users_df.info())

print("First Few Rows of Products Data:")
print(products_df.head())

print("First Few Rows of Transactions Data:")
print(transactions_df.head())

print("First Few Rows of Users Data:")
print(users_df.head())

#Identification of misisng values for data quality and completeness - Gives us an understanding for missing data

print("Missing Values in Products Table:")
print(products_df.isnull().sum())

print("Missing Values in Transactions Table:")
print(transactions_df.isnull().sum())

print("Missing Values in Users Table:")
print(users_df.isnull().sum())

#Identification of duplicate values for data quality and completeness - Gives us an understanding for repeated data

print("Products Table Duplicates:")
print(products_df.duplicated().sum())

print("Transactions Table Duplicates:")
print(transactions_df.duplicated().sum())

print("Users Table Duplicates:") 
print(users_df.duplicated().sum())

#Converting Data Types to standardized format and using coerce for null values and errors
users_df["CREATED_DATE"] = pd.to_datetime(users_df["CREATED_DATE"], errors="coerce")
users_df["BIRTH_DATE"] = pd.to_datetime(users_df["BIRTH_DATE"], errors="coerce")
transactions_df["PURCHASE_DATE"] = pd.to_datetime(transactions_df["PURCHASE_DATE"], errors="coerce")
transactions_df["SCAN_DATE"] = pd.to_datetime(transactions_df["SCAN_DATE"], errors="coerce")

#Convert BARCODE to string 
products_df["BARCODE"] = products_df["BARCODE"].astype("float64").astype("str")
transactions_df["BARCODE"] = transactions_df["BARCODE"].astype("float64").astype("str")

print("Data Types After Conversion:")
print(users_df.dtypes, transactions_df.dtypes, products_df.dtypes)

#Handling missing values

#Fill missing product categories with "Unknown"
products_df.fillna({"CATEGORY_3": "Unknown", "CATEGORY_4": "Unknown",
                    "MANUFACTURER": "Unknown", "BRAND": "Unknown"}, inplace=True)

# Fill missing values in transactions with "Unknown"
transactions_df["BARCODE"].fillna("Unknown", inplace=True)

# Fill missing values in users
users_df.fillna({"STATE": "Unknown", "LANGUAGE": "Unknown", "GENDER": "Unknown"}, inplace=True)



# Merge Transactions with Products
merged_df = transactions_df.merge(products_df, on="BARCODE", how="left")

# Convert FINAL_SALE to Numeric
merged_df["FINAL_SALE"] = pd.to_numeric(merged_df["FINAL_SALE"], errors="coerce")

# Handle missing values in BRAND column
merged_df["BRAND"] = merged_df["BRAND"].fillna("Unknown Brand")

# Aggregate Total Sales by Brand
top_brands = merged_df.groupby("BRAND")["FINAL_SALE"].sum().reset_index()

# Sort and select top 5 brands
top_brands = top_brands.sort_values(by="FINAL_SALE", ascending=False).head(5)






#Bar Chart for Top 5 Stores by Transactions

# Group by Category and Sum Sales
category_sales = merged_df.groupby("CATEGORY_1")["FINAL_SALE"].sum().nlargest(5)


# Get Top 5 Stores by Transaction Count
top_stores = transactions_df["STORE_NAME"].value_counts().nlargest(5)

# Plot Horizontal Bar Chart with Adjustments
plt.figure(figsize=(12, 6))
ax = sns.barplot(y=top_stores.index, x=top_stores.values, palette="coolwarm")


# Add Titles and Labels
plt.title("🏪 Top 5 Stores by Transactions", fontsize=16, fontweight="bold")
plt.xlabel("Number of Transactions", fontsize=12)
plt.ylabel("Store Name", fontsize=12)

# Display values on bars for clarity
for index, value in enumerate(top_stores.values):
    ax.text(value + 500, index, str(value), va="center", fontsize=12, color="black")

# Adjust layout for better readability
plt.xlim(0, max(top_stores.values) * 1.1)  # Extend x-axis slightly
plt.grid(axis="x", linestyle="--", alpha=0.7)  # Subtle grid lines

plt.show()






#Pie chart for Distribution of Sales by Generation

# Convert BIRTH_DATE to datetime format
users_df["BIRTH_DATE"] = pd.to_datetime(users_df["BIRTH_DATE"], errors="coerce")

# Categorize Generations
def get_generation(birth_year):
    if birth_year >= 1997:
        return "Gen Z"
    elif birth_year >= 1981:
        return "Millennials"
    elif birth_year >= 1965:
        return "Gen X"
    else:
        return "Boomers"

users_df["Generation"] = users_df["BIRTH_DATE"].dt.year.apply(lambda x: get_generation(x) if pd.notnull(x) else "Unknown")

# Merge Transactions with Users
merged_df = transactions_df.merge(users_df, left_on="USER_ID", right_on="ID", how="left")

# Convert FINAL_SALE to Numeric
merged_df["FINAL_SALE"] = pd.to_numeric(merged_df["FINAL_SALE"], errors="coerce")

# Group by Generation
generation_sales = merged_df.groupby("Generation")["FINAL_SALE"].sum().reset_index()

# Plot the Distribution
plt.figure(figsize=(10, 5))
sns.barplot(data=generation_sales, x="Generation", y="FINAL_SALE", palette="coolwarm")
plt.title("Total Sales by Generation")
plt.ylabel("Total Sales ($)")
plt.xlabel("Generation")
plt.show()








#Connecting to postgreSQL instance on docker
from sqlalchemy import create_engine

# Define PostgreSQL connection parameters
db_user = "myuser"
db_password = "mypassword"
db_name = "mydatabase"
db_host = "localhost"  # Use Docker container name (or "localhost" if running locally)
db_port = "5433"  # Default PostgreSQL port inside Docker

# Create the database engine
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# Load data into SQL tables
products_df.to_sql("products", engine, if_exists="replace", index=False)
transactions_df.to_sql("transactions", engine, if_exists="replace", index=False)
users_df.to_sql("users", engine, if_exists="replace", index=False)

print("Data Successfully Stored in PostgreSQL!")


