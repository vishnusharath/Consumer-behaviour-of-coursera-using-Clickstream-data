import json
import pandas as pd
from datetime import datetime
from ua_parser import user_agent_parser

if __name__ == '__main__':
    """
    Assigning an empty array to store the dataset
    """
    counter = 0
    click_data = []
    for line in open('psy-001_clickstream_export.txt', 'r'):
        json_val = json.loads(line)
        # val = pd.io.json.json_normalize(json_val)
        click_data.append(json_val)
        counter += 1
        if counter == 1001:
            break

    """
    To print the whole dataset
    """
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', -1)

    df = pd.DataFrame.from_dict(click_data)
"""
code to remove the regular expressions from the data and the  nested column 
"""
new = df['value'].str.split(",", expand=True)

print(len(new.columns))

for i in range(len(new.columns)):
    if i == len(new.columns) - 1:
        split_colon = new[i].str.split(":", expand=True)
        ident = split_colon[0][0].split('"')[1]
        split_brac = split_colon[1].str.split("}", expand=True)
        df[ident] = split_brac[0]
    else:
        split_colon = new[i].str.split(":", expand=True)
        ident = split_colon[0][0].split('"')[1]
        df[ident] = split_colon[1]

"""
Dropping the split column to avoid redundancy
"""
df = df.drop(columns="value")
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Converting timestamp to human readable
df.drop(df.columns[[0, 1]], axis=1, inplace=True)  # To remove the unwanted first two columns

"""
Code snippet to split the OS and browser name from User agent
"""
df['User browser'] = 'dummy'
for index, row in df.iterrows():
    # print(row['user_agent'])
    ua_string = row['user_agent']
    parsed_string = user_agent_parser.ParseUserAgent(ua_string)
    # print(parsed_string['family'])
    df.at[index, 'User browser'] = parsed_string['family']

df['User Device/OS'] = 'dummy'
for index, row in df.iterrows():
    # print(row['user_agent'])
    ua_string = row['user_agent']
    parsed_string = user_agent_parser.ParseOS(ua_string)
    print(parsed_string['family'])
    df.at[index, 'User Device/OS'] = parsed_string['family']  # To replace dummy as the value found

    """
    Code to convert to Excel #uncomment to save the excel file
   

    writer = pd.ExcelWriter('click_1L.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})
    df.to_excel(writer, sheet_name='1L values')
    writer.save()
 """
# print(df['User browser'])
#
# print(df.head(20))

"""
# Code to convert to Excel
#
# writer = pd.ExcelWriter('click_combined_10000.xlsx', engine='xlsxwriter',options={'strings_to_urls': False})
# df.to_excel(writer, sheet_name='10000 values')
# writer.save()
#
# """
"""
Code to convert to CSV

# # writer = pd.ExcelWriter('click_combined_100000.csv', engine='xlsxwriter',options={'strings_to_urls': False})
# writer = df.to_csv('click_combined_100000.csv', sep='\t', encoding='utf-8')
# writer.save()
"""
