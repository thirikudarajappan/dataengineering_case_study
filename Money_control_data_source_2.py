#!/usr/bin/env python
# coding: utf-8

# In[119]:


import requests
import pandas as pd
from pymongo import MongoClient
from bs4 import BeautifulSoup
import re
import json
import matplotlib.pyplot as plt


# In[120]:


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
        cli.close()
        
        
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
        


# In[121]:


req = requests.request('GET', 'https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI')
sbi = BeautifulSoup(req.content)


# In[122]:


# volum= sbi.find_all('div',{'id':"nse_vol"})
# print(sbi.find_all('div', {'id':"nsecp"}))

# for text in sbi.find_all('div',{'id':"nse_vol"}):
#     print(text.text)
    
def extractVolum(node):
    for text in node.find_all('div',{'id':"nse_vol"}):
        return text.text
def extractPrice(node):
    for text in node.find_all('div', {'id':"nsecp"}):
        return text.text
    


# In[123]:


from datetime import datetime
from threading import Timer
sbi_data_collection = []
def getStockDetail():
    now = datetime.now()
    req = requests.request('GET', 'https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI')
    sbi = BeautifulSoup(req.content)
    sbi_volume = extractVolum(sbi)# sbi.find_all('div',{'id':"nse_vol"})
#     print(sbi_volume)
    sbi_current_price=extractPrice(sbi)
#     print(sbi_current_price)
    sbi_current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    current = {
        'current_price': sbi_current_price, 'volume': sbi_volume, 'datetime': sbi_current_time
    }
#     print(current,'  Time')
    sbi_data_collection.append(current)
#     cli = MongoClient('mongodb://127.0.0.1:27017/')
#     db = cli.database
#     collection = db.moneycontrolCollection
# #     collection.insert_many(self.buyData)
#     cursor = collection.find({'script':'State Bank of India'})
   


# In[124]:


getStockDetail() 


# In[125]:


# timer = Timer(5, getStockDetail())
# timer.start()
sbi_data_collection


# In[126]:


from threading import Timer
def hello():
    getStockDetail()
#     sbi_data_collection
    Timer(30.0, hello).start()

Timer(30.0, hello).start()


# In[127]:


# import sched, time
# def dostuff():
#   print("stuff is being done!")
#   s.enter(3, 1, dostuff, ())

# s = sched.scheduler(time.time, time.sleep)
# s.enter(3, 1, dostuff, ())
# s.run()


# In[128]:


df = pd.DataFrame(sbi_data_collection)


# In[129]:


df


# In[130]:


# df.plot(kind="line",index='datetime', y='current_price',x='volume')


# In[131]:


import matplotlib.pyplot as plt


# In[133]:


# df.plot(kind = 'line', x = 'datetime', y = 'volume')

# plt.show()


# In[ ]:




