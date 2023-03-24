import pandas as pd

# Read in the tables
table1 = pd.read_csv('table1.csv')
table2 = pd.read_csv('table2.csv')

# Create an empty list to store the matching rows
matches = []

# Iterate through each row in table1
for index, row in table1.iterrows():
    # Check if column3 of table1 is equal to column3 of table2
    if row['column3'] in table2['column3'].values:
        # Get the matching rows from table2
        matches = table2[table2['column3'] == row['column3']]
        # Iterate through the matching rows
        for match in matches:
            # Check if column1 of table1 is a substring of another column1 in table2
            if match['column1'].contains(row['column1']) != -1:
                # Check if column2 of table1 is a substring of another column2 in table2
                if match['column2'].find(row['column2']) != -1:
                    # Copy column4 values from table2 to column4 in table1
                    table1.at[index, 'column4'] = match['column4']

# Print the updated table1
print(table1)
