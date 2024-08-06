# Sample Game-of-Thrones Data

We found a sample Game of Thrones dataset on * [Kaggle](https://www.kaggle.com/datasets/mmmarchetti/game-of-thrones-dataset)

If two names were mentioned within 15 words a link count was created:

```
Source,Target,Type,weight,book
Addam-Marbrand,Jaime-Lannister,Undirected,3,1
Addam-Marbrand,Tywin-Lannister,Undirected,6,1
Aegon-I-Targaryen,Daenerys-Targaryen,Undirected,5,1
Aegon-I-Targaryen,Eddard-Stark,Undirected,4,1
Aemon-Targaryen-(Maester-Aemon),Alliser-Thorne,Undirected,4,1
```

We first want to create a list of vertices that include all the people's names, both Source and Target names should be included.

## Loading People

Although there are ways to do this with the GUI, I created a simple Python program that creates a single list of people.

```py
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
```

The people names file now looks like this:

```
Names
Addam-Marbrand
Aegon-I-Targaryen
Aemon-Targaryen-(Maester-Aemon)
Aerys-II-Targaryen
Aggo
Albett
Alliser-Thorne
Alyn
```

This can then be loaded using the "Load Data" 