import pandas as pd
import openpyxl 

# Load the CSV
df = pd.read_csv("data/train.csv")

pd.set_option('display.max_columns', None)

# Calculate the mean of the Age column
age_mean = df['Age'].mean()

# Replace missing values in the Age column with the mean
df['Age'].fillna(age_mean, inplace=True)

# Verify that there are no missing values in the Age column
print("\nNumber of Missing Values in Age column:")
print(df['Age'].isnull().sum())

# round the values of the Age column
df['Age'] = df['Age'].round()

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Round the values in the Age column
df['Age'] = df['Age'].round()

# Define a function to categorize age
def categorize_age(age):
  if age <= 14:
    return 'Children'
  elif 15 <= age <= 64:
    return 'Youth&Adults'
  else:
    return 'Seniors'

# Create the 'age_category' column
df['age_category'] = df['Age'].apply(categorize_age)

df.head(10)
print(df['age_category'].value_counts())

# Export the DataFrame to an Excel file
df.to_excel('titanic_output.xlsx', index=False, engine='openpyxl')

print("\nData has been exported to titanic_output.xlsx")