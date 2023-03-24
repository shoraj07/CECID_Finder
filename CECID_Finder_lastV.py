import numpy
import pandas as pd
import numpy as np

'''reading data from input file.
   
   Please add the files in the same order.'''
df1 = pd.read_excel(r'Input\case_soc-mark-0109.xlsx')
df2 = pd.read_excel(r'Input\involved_party-mark-0109.xlsx')

df2.User_Id__c.fillna(0, inplace=True) # Replacing the blank spaces in "User ID" column with 0.
df1.Id.fillna(0, inplace=True) # Replacing the blank spaces in "User ID" column with 0.
df2.replace(0, np.nan , inplace=True)  # Replacing '0' with 'NaN'.
df1.replace(0, np.nan , inplace=True)  # Replacing '0' with 'NaN'.
df2.dropna(subset=['User_Id__c'],inplace=True) # Droping 'NaN' cells from "User ID"(removing empty cells from User ID).
df1.dropna(subset=['Id'],inplace=True) # Droping 'NaN' cells from "User ID"(removing empty cells from User ID).

''' empName- contains value from "Subject_of_Case__c"
    firstName- contains first name after splitting
    lastName- contains last name after splitting'''
empName = df1.Subject_of_Case__c.values.tolist()
firstName = []
lastName = []

'''split the names in empName to firstName and lastName'''
try:
    for name in empName:
        if str(name).__contains__(','):
            lastName.append(name.split(', ', 1)[0])
            firstName.append(name.split(', ', 1)[1])
        else:
            firstName.append(name.split(' ', 1)[0])
            lastName.append(name.split(' ', 1)[1])
except:
    print(name)

'''Adding data from lists(firstName, lastName) in df1
   df1['Full Name']- creating a primary key to compare names in both the sheets.'''
df1['First Name'] = firstName
df1['Last Name'] = lastName
df1['Full Name'] = df1['First Name'] + df1['Last Name']

# df2.User_Id__c.fillna(0, inplace=True) # Replacing the blank spaces in "User ID" column with 0.
# df2.replace(0, np.nan , inplace=True)  # Replacing '0' with 'NaN'.
# df2.dropna(subset=['User_Id__c'],inplace=True) # Droping 'NaN' cells from "User ID"(removing empty cells from User ID).

df2['Full Name'] = df2['First_Name__c'] + df2['Last_Name__c'] # Creating a new column consisting both first and last name.
df2 = df2[['Full Name', 'User_Id__c', 'Case_Number__c']] # Filtering out the un-necessary columns from the data sheet.

df1["Full Name"] = df1["Full Name"].str.replace("[?, ' ']","")
df2["Full Name"] = df2["Full Name"].str.replace("[?, ' ']","")
# df1["Full Name"] = df1["Full Name"].str.replace("[' ']","")
# df2["Full Name"] = df2["Full Name"].str.replace("[' ']","")


df2 = df2.drop_duplicates() # Removing Duplicates.

temp = pd.merge(df1, df2, left_on=['Full Name', 'Id'], right_on=['Full Name', 'Case_Number__c'], how='outer')
temp.drop_duplicates(inplace=True, ignore_index=True)
temp.drop(['First Name', 'Last Name', 'Full Name', 'Case_Number__c'], axis=1, inplace=True) # Filtering out the
                                                                            # un-necessary columns from the data sheet.

df1.to_excel('Output/case_soc1.xlsx', index=False) # case_soc
df2.to_excel('Output/involved_party2.xlsx', index=False) # involved_party
temp.to_excel('Output/CECID_Mapping_Output.xlsx', index=False)
