import pandas as pd

# Load data into dataframes
df1 = pd.read_csv("table1.csv")
df2 = pd.read_csv("table2.csv")

# Iterate through rows in table1
for i, row1 in df1.iterrows():
    # Iterate through rows in table2
    for j, row2 in df2.iterrows():
        # Check if column1 of table1 is a substring of column1 in table2
        # and column2 of table1 is a substring of column2 in table2
        # and column3 of table1 is equal to column3  of table2
        if (row1["Id"] in row2["Case_Number__c"]) and (row1["First Name"] in row2["First_Name__c"]) and (row1["Last Name"] == row2["Last_Name__c"]):
            # Copy column4 value from table2 to column4 in table1
            df1.at[i, "User_Id__c"] = row2["User_Id__c"]

# Save updated table1 to a new csv file
df1.to_csv("table1_updated.csv", index=False)

# can extend this way but causing issue as repeating the userId.

for i, row1 in df1.iterrows():
    # Iterate through rows in table2
    for j, row2 in df2.iterrows():
        # Check if column1 of table1 is a substring of column1 in table2
        # and column2 of table1 is a substring of column2 in table2
        # and column3 of table1 is equal to column3  of table2
        if (row1["Id"] == row2["Case_Number__c"]) and \
                (str(row1["First Name"]).lower() in str(row2["First_Name__c"]).lower()) or \
                (str(row1["First Name"]).lower().__contains__(str(row2["First_Name__c"]).lower())) and \
                (str(row1["Last Name"]).lower() == str(row2["Last_Name__c"]).lower()) or \
                (str(row1["Last Name"]).lower().__contains__(str(row2["Last_Name__c"]).lower())):
            # Copy column4 value from table2 to column4 in table1
            df1.at[i, "User_Id__c"] = row2["User_Id__c"]

