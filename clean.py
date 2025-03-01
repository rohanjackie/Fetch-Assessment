import pandas as pd

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
