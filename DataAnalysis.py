import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('bmh')  # style format for plotting

if __name__ == '__main__':
    df = pd.read_excel(r'click_1L.xlsx')

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', -1)
    print(df.head())

    # print(df.columns)
    #
    # print(df.head(5))

    print(df.shape)
    print(df.isnull().sum())

    df.drop(df.columns[[7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]], axis=1, inplace=True)
    print(df.isnull().sum())
    df = df.dropna(axis=0) # To drop the null rows in the from column
    print(df.isnull().sum())

"""
Removing the duplicates in the dataframe
"""
MUOS = (df.groupby(df['User Device/OS'])['username'].nunique().nlargest(10).reset_index(name='count'))
print(MUOS)
MOB = (df.groupby(df['User browser'])['username'].nunique().nlargest(10).reset_index(name='count'))
print(MOB)
MFU = (df.groupby(df['username']).size().nlargest(10).reset_index(name='count'))
print(MFU)
print(MFU.count(axis=0))

"""
Correcting the case mismatch in the dataset to avoid duplicates
"""

MUL = (df.groupby(df['language'].str.split(",", expand=True)[0].str.upper())['username'].nunique().nlargest(
    10).reset_index(name='count'))
print(MUL)
print(MUL.keys())

"""
Terminologies:
MUOS - MOST USED OPERATING SYSTEM
MOB - MOST USED BROWSER
MFU - MOST FREQUENT USER
MUL - MOST USED TO LANGUAGE
"""

"""
    Drawing charts for the insights

    """
"""
Bar Chart for plotting Most used OS
"""
plt.bar(range(len(MUOS['count'])), MUOS['count'])
plt.xlabel('Most used OS', fontsize=15)
plt.ylabel('No of Users', fontsize=15)
plt.xticks(range(len(MUOS['User Device/OS'])), MUOS['User Device/OS'])
plt.title('MOST USED OS FOR VIEWING')
plt.show(block=True)

"""
Code for plotting most used Browsers
"""

plt.bar(range(len(MOB['count'])), MOB['count'])
plt.xlabel('Most used Browsers', fontsize=15)
plt.ylabel('No of Users', fontsize=15)
plt.xticks(range(len(MOB['User browser'])), MOB['User browser'])
plt.title('MOST USED browsers FOR VIEWING')
plt.show(block=True)

"""
Code for plotting most active User
"""

plt.pie(MUL['count'], labels=MUL[0], autopct='%0.2f')
plt.axis('equal')
plt.title('MOST used language')
plt.show(block=True)

"""

The most active user is 0da7bb68bf6f29d10c5476af42de1f2c9c6ba153 with the IP address 46.10.19.106


client            0    
from              2455 
key               0    
language          0    
page_url          0    
session           0    
timestamp         0    
user_agent        0    
user_ip           0    
username          0    
currentTime       44652
playbackRate      51969
paused            44650
error             98978
networkState      46673
readyState        46673
eventTimestamp    44766
initTimestamp     44766
type              44766
prevTime          44768
User browser      0    
User Device/OS    0    
client            0
from              0
key               0
language          0
page_url          0
session           0
timestamp         0
user_ip           0
username          0
User browser      0
User Device/OS    0

                                    username  count
0  0da7bb68bf6f29d10c5476af42de1f2c9c6ba153  1060 
1  d333771a15bba985586d6ec53db437855b2f1cc7  979  
2  756817966ea3918aa14ed2b50b2184cbbc2ccb81  731  
3  7141d9efcbea448b931eea78c0af123da610a3b1  707  
4  d851f993a4d0a439cd1b16a1968523b5b4f34d40  664  
5  910a0e6309bdf253ba7a33e9e6a3fe14db7f6e74  584   
print(df.groupby(df['User Device/OS'])['username'].nunique())
print(df['username'].nunique())  # Count the unique number of users
print(df.groupby(df['User Device/OS']).size().nlargest(5)) #Count with the duplicates

"""
