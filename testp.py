#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      oranj
#
# Created:     29.05.2018
# Copyright:   (c) oranj 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pandas as pd
import re
df = pd.read_csv('us-cities.csv',encoding = "ISO-8859-1",sep=',')
df = df.drop(['latitude', 'longitude','area_code','households','land_area','water_area','time_zone'], axis=1)
df = df.sort_values(by='population',ascending=False)
print(df)
df = df.drop_duplicates(subset=['name', 'state_code'])

df.to_csv('usunique.csv',sep=';',index=False)


