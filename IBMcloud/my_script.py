import pandas as pd

# URL to the CSV file
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_path)

# Display the first few rows of the DataFrame
print(df.head())

# Select the 'Length' column
x = df[['Length']]
print(x)

# Select the 'Artist' column and check its type
x = df[['Artist']]
print(type(x))  # This will output: <class 'pandas.core.frame.DataFrame'>

# Select multiple columns: 'Artist', 'Length', 'Genre'
y = df[['Artist', 'Length', 'Genre']]
print(y)

# Access elements using iloc
print(df.iloc[0, 0])  # First row, first column
print(df.iloc[1, 0])  # Second row, first column
print(df.iloc[0, 2])  # First row, third column
print(df.iloc[1, 2])  # Second row, third column

# Access elements using loc
print(df.loc[0, 'Artist'])  # First row, 'Artist' column
print(df.loc[1, 'Artist'])  # Second row, 'Artist' column
print(df.loc[0, 'Released'])  # First row, 'Released' column
print(df.loc[1, 'Released'])  # Second row, 'Released' column

# Slicing DataFrame using iloc
print(df.iloc[0:2, 0:3])  # First two rows, first three columns

# Slicing DataFrame using loc
print(df.loc[0:2, 'Artist':'Released'])  # First three rows, columns from 'Artist' to 'Released'

q = df[['Rating']]
print('Rating dataFrame: ',q)
