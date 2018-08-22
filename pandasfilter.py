#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      oranj
#
# Created:     30.05.2018
# Copyright:   (c) oranj 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pandas as pd
'''
df = pd.read_csv('free-zipcode-database.csv')
print(df.City)
data = pd.read_csv('alternativeloans.csv')
data['zip']=0
print(data)
for index, row in df.iterrows():
    data.zip[data.city==row['City'].lower().capitalize()][data.state==row['State']] = row['Zipcode']
    print(index/len(df))
data.to_csv('alternativeloans1.csv')
'''

filename = 'financialservices.csv'
df = pd.read_csv(filename,error_bad_lines=False,encoding = "ISO-8859-1",sep=',')

print(len(df.name.unique()))
dflen = len(df)
for x in df.name.unique():
    df=df.append({'name': x}, ignore_index=True)
last = df.tail(len(df.name.unique()))
df['parent']=0

print(df)
for index, row in last.iterrows():
    print (row['name'])
    df.parent[df.name==row['name']] = row['name']
    print(index)

df.to_csv(filename,sep=';')

cities=pd.read_csv('us-cities.csv')
df = pd.read_csv(filename,sep=";")
df2 = cities.drop_duplicates(subset=['state'], keep='first')
print(df2.state)

for index, row in df2.iterrows():
    df.state[df.state==row['state_code']]=row['state']
    print(row)
print(df)
df.to_csv(filename,sep=';')
