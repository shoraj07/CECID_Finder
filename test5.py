import pandas as pd

mask = (table1['column3'] == table2['column3']) & \
       (table1['column1'].str.contains(table2['column1'])) & \
       (table1['column2'].str.contains(table2['column2']))

# Use the mask to filter the rows of table1
table1.loc[mask, 'column4'] = table2.loc[mask, 'column4']

'''
merged_df = pd.merge(df1, df2, left_on='Id', right_on='Case_Number__c', how='inner')

mask = (merged_df['Id'] == merged_df['Case_Number__c']) & \
       (merged_df['First Name'].str.contains(merged_df['First_Name__c'])) & \
       (merged_df['Last Name'].str.contains(merged_df['Last_Name__c']))

# Use the mask to filter the rows of table1
df1.loc[mask, 'User_Id__c'] = df2.loc[mask, 'User_Id__c']
'''