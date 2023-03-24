import pandas as pd
import numpy as np

'''reading data from input file.

   Please add the files in the same order.'''
df1 = pd.read_excel(r'Input\case_soc-mark-0109(2)-shoraj-01-23-23.xlsx')
df2 = pd.read_excel(r'Input\involved_party-mark-0109(2)-shoraj-01-23-23.xlsx')

df2.User_Id__c.fillna(0, inplace=True)  # Replacing the blank spaces in "User ID" column with 0.
df1.Id.fillna(0, inplace=True)  # Replacing the blank spaces in "User ID" column with 0.
df2.replace(0, np.nan, inplace=True)  # Replacing '0' with 'NaN'.
df1.replace(0, np.nan, inplace=True)  # Replacing '0' with 'NaN'.
df2.dropna(subset=['User_Id__c'],
           inplace=True)  # Droping 'NaN' cells from "User ID"(removing empty cells from User ID).
df1.dropna(subset=['Id'], inplace=True)  # Droping 'NaN' cells from "User ID"(removing empty cells from User ID).

''' empName- contains value from "Subject_of_Case__c"
    firstName- contains first name after splitting
    lastName- contains last name after splitting'''
empName = df1.Subject_of_Case__c.values.tolist()
firstName = []
lastName = []
matches = []

'''split the names in empName to firstName and lastName'''
for name in empName:
    if str(name).__contains__(','):
        lastName.append(name.split(', ', 1)[0])
        firstName.append(name.split(', ', 1)[1])
    else:
        firstName.append(name.split(' ', 1)[0])
        lastName.append(name.split(' ', 1)[1])



'''Adding data from lists(firstName, lastName) in df1
   df1['Full Name']- creating a primary key to compare names in both the sheets.'''
df1['First Name'] = firstName
df1['Last Name'] = lastName



# Iterate through each row in df1
for index, row in df1.iterrows():
    if row['First Name'].__contains__('?') or row['Last Name'].__contains__('?'):
        # row['First Name'].split(', ', 1)[0]
        row['First Name'] = row['First Name'].split('?', 1)[0]
        row['Last Name'] = row['Last Name'].split('?', 1)[0]
        # print('containing ? in the first value--------------------------',row['First Name'])
        # print('containing ? in the last value--------------------------',row['Last Name'])
    # Check if column3 of df1 is equal to column3 of df2
    if row['Id'] in df2['Case_Number__c'].values:
        # Get the matching rows from df2
        matches = df2[df2['Case_Number__c'] == row['Id']]
        # Iterate through the matching rows
        for i, match in matches.iterrows():
            # Check if column1 of table1 is a substring of another column1 in table2
            if row['First Name'] in match['First_Name__c'] or row['First Name'].__contains__(match['First_Name__c'])\
                    or match['First_Name__c'].__contains__(row['First Name']):
                # Check if column2 of table1 is a substring of another column2 in table2
                if row['Last Name'] in match['Last_Name__c'] or row['Last Name'].__contains__(match['Last_Name__c']) \
                    or match['Last_Name__c'].__contains__(row['Last Name']):
                    # Copy column4 values from table2 to column4 in table1
                    df1.at[index, 'User_Id__c'] = match['User_Id__c']

final_values = df1.__deepcopy__()
final_values.User_Id__c.fillna(0, inplace=True)  # Replacing the blank spaces in "User ID" column with 0.
final_values.Id.fillna(0, inplace=True)  # Replacing the blank spaces in "User ID" column with 0.
final_values.replace(0, np.nan, inplace=True)  # Replacing '0' with 'NaN'.
final_values.replace(0, np.nan, inplace=True)  # Replacing '0' with 'NaN'.
final_values.dropna(subset=['User_Id__c'],
           inplace=True)  # Droping 'NaN' cells from "User ID"(removing empty cells from User ID).

final_values.to_excel('Output/CECID_Mapping_Output.xlsx', index=False)
df1.to_excel('Output/case_soc1.xlsx', index=False)  # case_soc
df2.to_excel('Output/involved_party2.xlsx', index=False)  # involved_party
