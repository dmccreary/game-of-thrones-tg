import pandas as pd

# Load the CSV file
file_path = '../data/book1.csv'
data = pd.read_csv(file_path)

# Assuming the first two columns contain person names
names_col1 = data.iloc[:, 0].dropna().unique()
names_col2 = data.iloc[:, 1].dropna().unique()

# Combine and get unique names
unique_names = set(names_col1).union(set(names_col2))
unique_names = sorted(unique_names)

# Create a new DataFrame and save to CSV
unique_names_df = pd.DataFrame(unique_names, columns=["Names"])
output_path = '../data/book1-people.csv'
unique_names_df.to_csv(output_path, index=False)

output_path
