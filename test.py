import pandas as pd
from tabulate import tabulate
import numpy as np
'''reading data from input file.'''
df1 = pd.read_excel(r'Input\case_soc-shoraj-12-15-22.xlsx')
df2 = pd.read_excel(r'Input\involved_party-shoraj-12-16-22.xlsx')

''' empName- contains value from "Subject_of_Case__c"
    firstName- contains first name after splitting
    lastName- contains last name after splitting'''
empName = df1.Subject_of_Case__c.values.tolist()
firstName = []
lastName = []

'''split the names in empName to firstName and lastName'''
for name in empName:
    if str(name).__contains__(','):
        lastName.append(name.split(', ', 1)[0])
        firstName.append(name.split(', ', 1)[1])
    else:
        firstName.append(name.split(' ', 1)[0])
        lastName.append(name.split(' ', 1)[1])

# temp1 = df1
# temp1['First Name'] = firstName
# temp1['Last Name'] = lastName
# temp1['Full Name'] = temp1['First Name'] + temp1['Last Name']
df1['First Name'] = firstName
df1['Last Name'] = lastName
df1['Full Name'] = df1['First Name'] + df1['Last Name']

# temp2 = df2
# temp2['Full Name'] = temp2['First_Name__c'] + temp2['Last_Name__c']
# temp2 = temp2[['Full Name', 'User_Id__c']]
# temp2 = temp2.drop_duplicates()
df2['Full Name'] = df2['First_Name__c'] + df2['Last_Name__c']
df2 = df2[['Full Name', 'User_Id__c']]
df2 = df2.drop_duplicates()

temp3 = pd.merge(df1, df2, on=['Full Name'], how='inner')
temp3.drop_duplicates(inplace=True, ignore_index=True)
temp3.drop(['First Name', 'Last Name', 'Full Name'], axis=1, inplace=True)

df1.to_excel('Output/temp1.xlsx', index=False)
df2.to_excel('Output/temp2.xlsx', index=False)
temp3.to_excel('Output/temp3.xlsx', index=False)
