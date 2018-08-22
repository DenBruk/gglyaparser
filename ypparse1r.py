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
# -*- coding: utf-8 -*-
from grab import Grab
import pandas as pd
import re
g = Grab()
df = pd.read_csv('us-cities.csv')
dfuniquestates = df.state_code.unique()
names = []
phones = []
cities = []
streets = []
websites = []
states = []
ids=[]
iter=0;
import math
for state in dfuniquestates[38:]:
    print(dfuniquestates)
    print(state)
    notfound=0
    iter+=1
    print(iter/len(dfuniquestates))
    ids=[]
    d = {}
    names = []
    phones = []
    cities = []
    streets = []
    websites = []
    states = []
    ids=[]
    df.iloc[0:0]
    g.go('https://www.yellowpages.com/search?search_terms=financial+services&geo_location_terms='+state+"&page="+str(1))
    for i in range(math.ceil(int(re.findall('\d+', g.xpath_text('//*[@id="main-content"]/div[2]/div[4]/p' ))[0])/30)):
        ids=[]
        i+=1
        print(i)
        g.go('https://www.yellowpages.com/search?search_terms=financial+services&geo_location_terms='+state+"&page="+str(i))
        for elem in g.doc.select('//div[@class="result"]'):
            ids.append(elem.attr('id'))

        for id in ids:
            try:
                names.append(g.xpath('//*[@id="'+str(id)+'"]/div/div[2]/div[2]/h2/a/span').text_content())
            except:
                names.append(g.xpath('//*[@id="'+str(id)+'"]/div/div[2]/div[3]/h2/a/span').text_content())
            try:
                streets.append(g.xpath('//*[@id="'+str(id)+'"]/div/div[2]/div[2]/div[1]/p/span[1]').text_content())
            except:
                streets.append(None)

            try:
                cities.append(g.xpath('//*[@id="'+str(id)+'"]/div/div[2]/div[2]/div[1]/p/span[2]').text_content())
            except:
                cities.append(None)
            try:
                phones.append(g.xpath('//*[@id="'+str(id)+'"]/div/div[2]/div[2]/div[1]/div').text_content())
            except:
                try:
                    phones.append(g.xpath('//*[@id="'+str(id)+'"]/div/div[2]/div[3]/div[1]/div[2]').text_content())
                except:
                    try:
                        phones.append(g.xpath('//*[@id="'+str(id)+'"]/div/div[2]/div[3]/div[1]/div').text_content())
                    except:
                        phones.append(None)
            try:
                websites.append(g.xpath_text('//*[@id="'+str(id)+'"]/div/div[2]/div[2]/div[2]/div[2]/a[1]/@href'))
            except:
                try:
                    websites.append(g.xpath_text('//*[@id="'+str(id)+'"]/div/div[2]/div[3]/div[2]/div[2]/a[1]/@href'))
                except:
                    websites.append(None)
            states.append(state)
    d = {'Name':names,'street':streets,'phone':phones,'city':cities,'website':websites,'state':states}
    df = pd.DataFrame(d)
    with open('financialservices.csv', 'a',encoding='utf-8') as f:
        df.to_csv(f, header=False)

