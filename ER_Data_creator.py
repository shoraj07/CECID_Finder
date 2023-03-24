import pandas as pd
import numpy as np

'''reading data from input file.

   Please add the files in the same order.'''
df1 = pd.read_excel(r'D:\BI- Mark\CECID- Finder\01-30-23\Copy\CECID_Mapping_Output-shoraj-01-30-23.xlsx')
df2 = pd.read_excel(r'D:\BI- Mark\CECID- Finder\01-30-23\Copy\ER Report (all)-2023-01-30-02-18-45-shoraj-01-30-23 - Copy.xlsx')

merged_df = pd.merge(df1, df2, left_on=['CaseNumber','Subject_of_Case__c'],
                     right_on=['Case Number','Subject of Case'], how='right')

merged_df.to_excel(r'D:\BI- Mark\CECID- Finder\01-30-23\Copy\output.xlsx')