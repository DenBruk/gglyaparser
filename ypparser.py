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

from grab import Grab
import pandas as pd
import re
g = Grab()
df = pd.read_csv('us-cities.csv')
dfuniquestates = df.state_code.unique()
names = []
phones = []
adresses = []
infos=[]
iter=0;
import math
for state in dfuniquestates[:1]:
    print(state)
    notfound=0
    iter+=1
    g.go('https://www.yellowpages.com/search?search_terms=payday+loans&geo_location_terms='+state+"&page="+str(1))
    for i in range(math.ceil(int(re.findall('\d+', g.xpath_text('//*[@id="main-content"]/div[2]/div[4]/p' ))[0])/30)):
        print(i)
        g.go('https://www.yellowpages.com/search?search_terms=payday+loans&geo_location_terms='+state+"&page="+str(i+1))
        for elem in g.doc.select('//h2[@class="n"]'): #имя
            name=" "
            name = elem.text()
            if(name.find('.')!=-1):
                names.append(name)
            else:
                continue
        for elem in g.doc.select('//div[@class="info-section info-primary"]'):
            info = (elem.text())
            infos.append(info)
            print(infos)
        i+=1
    print(iter/len(dfuniquestates))
import csv
print(len(names),len(infos))
d = {'Name':names,'Ad':infos}
df = pd.DataFrame(d)
df.to_csv('output.csv')

