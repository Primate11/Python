#!/usr/bin/env python
# coding: utf-8

# In[98]:


# import the libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[136]:



# Connect to Website and pull in data

URL = "https://www.amazon.fr/dp/B09H7N8DHY/ref=sspa_dk_detail_5?psc=1&pd_rd_i=B09H7N8DHY&pd_rd_w=IS7GW&content-id=amzn1.sym.d9b1a9d1-cd4a-47bf-8586-2b11bbbee16b&pf_rd_p=d9b1a9d1-cd4a-47bf-8586-2b11bbbee16b&pf_rd_r=V4M8Z5PB9GC1WXX6ZDGR&pd_rd_wg=6BfSN&pd_rd_r=1da356a2-b5fd-406f-a553-81ebd08c8e3c&s=computers&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFFWTk5TElSSlo4VkomZW5jcnlwdGVkSWQ9QTAzMDM5OTMxTVg3WEZTQzg4TVQyJmVuY3J5cHRlZEFkSWQ9QTEwMDEzMjM5QzdOVzhSUzExODQmd2lkZ2V0TmFtZT1zcF9kZXRhaWwyJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-62f20c41-2d5329047afc2a9202eaf25f"}

page = requests.get(URL, headers=headers)

#Object1
soup1 = BeautifulSoup(page.content, "html.parser")
#Object2
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

product = soup2.find(id='productTitle').get_text()
price = soup2.find(class_='a-offscreen').get_text()
évaluations = soup2.find(id='acrCustomerReviewText', class_='a-size-base').get_text()
rating = soup2.find(class_='a-icon a-icon-star a-star-5').get_text()

print(product)
print(price)
print(évaluations)
print(rating)


# In[137]:


# Clean up the data a little bit

import re

product = (product).strip( )
price = (price).strip( )
rating = (rating).strip( )
évaluation = (évaluations).strip( )



print(product)
print(price)
print(rating)
print(évaluation)


# In[123]:


# Create a Timestamp for your output to track when data was collected

import datetime
from datetime import datetime

date = datetime.now()
datetime = date.strftime("%d/%m/%Y %H:%M:%S")

print(datetime)


# In[140]:


# Create CSV and write headers and data into the file
import csv 

header = ['product', 'price', 'rate', 'évaluation' ,'datetime' ]
data = [product, price, rate,évaluation, datetime]


with open('ScrapeAmazonTry.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    

import pandas as pd

df = pd.read_csv(r'C:\Users\igieo\ScrapeAmazonTry.csv')

print(df)


# In[144]:


#Appending data to the csv

with open('ScrapeAmazonTry.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)
    
print(df)


# In[145]:


#Combine all of the above code into one function 
#To be able to  run it automatically


def product_price():
   
    URL = "https://www.amazon.fr/dp/B09H7N8DHY/ref=sspa_dk_detail_5?psc=1&pd_rd_i=B09H7N8DHY&pd_rd_w=IS7GW&content-id=amzn1.sym.d9b1a9d1-cd4a-47bf-8586-2b11bbbee16b&pf_rd_p=d9b1a9d1-cd4a-47bf-8586-2b11bbbee16b&pf_rd_r=V4M8Z5PB9GC1WXX6ZDGR&pd_rd_wg=6BfSN&pd_rd_r=1da356a2-b5fd-406f-a553-81ebd08c8e3c&s=computers&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFFWTk5TElSSlo4VkomZW5jcnlwdGVkSWQ9QTAzMDM5OTMxTVg3WEZTQzg4TVQyJmVuY3J5cHRlZEFkSWQ9QTEwMDEzMjM5QzdOVzhSUzExODQmd2lkZ2V0TmFtZT1zcF9kZXRhaWwyJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-62f20c41-2d5329047afc2a9202eaf25f"}

    page = requests.get(URL, headers=headers)

    #Object1
    soup1 = BeautifulSoup(page.content, "html.parser")
    #Object2
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    product = soup2.find(id='productTitle').get_text()
    price = soup2.find(class_='a-offscreen').get_text()
    évaluations = soup2.find(id='acrCustomerReviewText', class_='a-size-base').get_text()
    rating = soup2.find(class_='a-icon a-icon-star a-star-5').get_text()

    import re

    product = (product).strip( )
    price = (price).strip( )
    rating = (rating).strip( )
    évaluation = (évaluations).strip( )

    import datetime
    from datetime import datetime

    date = datetime.now()
    datetime = date.strftime("%d/%m/%Y %H:%M:%S")

    import csv 

    header = ['product', 'price', 'rate', 'évaluation' ,'datetime' ]
    data = [product, price, rate,évaluation, datetime]


    with open('ScrapeAmazonTry.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    

    


# In[146]:


# Runs product_price after a set time and inputs data into your CSV

while(True):
    product_price()
    time.sleep(3)


# In[148]:




import pandas as pd

df = pd.read_csv(r'C:\Users\igieo\ScrapeAmazonTry.csv')

print(df)


# In[132]:





# In[ ]:




