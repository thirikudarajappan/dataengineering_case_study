#!/usr/bin/env python
# coding: utf-8

# In[52]:


import requests
import pandas as pd
from pymongo import MongoClient
from bs4 import BeautifulSoup
import re


# In[53]:


client = MongoClient('mongodb://127.0.0.1:27017/')
print("Connection Successful")


# In[118]:


class dataFromMoneyControl:
    buyData = []
    def __init__(self):
         self.httpRequet()
#         Extract

    def httpRequet(self):
        req = requests.request('GET', 'https://www.moneycontrol.com/news/business/stocks/page-%d/')
        soup = BeautifulSoup(req.content)
        self.onlyBuyCall(soup)
#         Transform
    def onlyBuyCall(self, soup):
        thisdict= {}
        href_tag_buy=soup.find_all(string=re.compile("^Buy"))
        for tag in href_tag_buy:
#          `
                print(tag.find('Buy '))
#             if tag.find('Buy '):
                temp = tag.split(';')
#                 target= temp[1].split(': ')[0].split('of ')[1]
#                 adviser = temp[1].split(': ')[1]
#                 print(target,' target')
#                 print(adviser, 'adviser')
                adStock = {
                    'type': 'Buy',
                    'script': temp[0].split('Buy ')[1],
                    'target': temp[1].split(': ')[0].split('of ')[1],
                    'adviser': temp[1].split(': ')[1]
                }
                self.buyData.append(adStock)
        self.storeData()
        
    def storeData(self):
        cli = MongoClient('mongodb://127.0.0.1:27017/')
        db = cli.database
        collection = db.moneycontrolCollection
        collection.insert_many(self.buyData)
        cursor = collection.find()
        for record in cursor:
            print(record)
        
        
#                 thisdict.update(adStock)
#                 print(thisdict)
#                 print(self.buyData)
#         self.dataFrame()
        
#     def dataDataFrame(self):
#         df = pd.DataFrame(self.buyData)
#         print(df)
            
            
#             buyData
#         print(href_tag_buy)
#         pf = pd.DataFrame(href_tag_buy)
#         print(pf)
        


# In[119]:


moneyControl = dataFromMoneyControl()
# buyCall = moneyControl.httpRequet()


# In[125]:


import json
df = pd.read_csv('SBIN.NS.csv')
print(df.to_string())


# In[128]:


df.info()
df.dropna(inplace = True)
df['Date'] = pd.to_datetime(df['Date'])


# In[129]:


import matplotlib.pyplot as pltdf.plot(kind = 'line', x = 'Date', y = 'Volume')

plt.show()


# In[141]:


df.plot(kind = 'line', x = 'Date', y = 'Volume')

plt.show()


# In[140]:


df.plot(kind = 'hist', x = 'Volume', y = 'Close')


# In[138]:


df.plot(kind = 'line', x = 'Date', y = 'Close')


# In[ ]:




