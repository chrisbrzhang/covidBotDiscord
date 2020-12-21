# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 12:11:39 2020

@author: doodo
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
from selenium.webdriver.chrome.options import Options 

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome("C:\\Users\doodo\\Documents\\Python Scripts\\Chrome_Driver\\chromedriver",options=options)

country=[]#List to store name of the country
Total_Cases=[] #List to store name of the product
New_Cases=[] #List to store price of the product
Total_Death=[] #List to store rating of the product
driver.get("https://www.worldometers.info/coronavirus/")
content = driver.page_source
soup = BeautifulSoup(content, features="lxml")


### GET COUNTRY NAME ####
for i in soup.findAll('a',href=True, attrs={'class':'mt_a'}):
    soupy = BeautifulSoup(str(i),'html.parser')
    tag = soupy.a
    country.append(tag.string)
    
### GET Total Cases####


    
Temp = []
for tag in soup.findAll('td',href=False):
    print(tag.string)
    Temp.append(tag.string)

# any(x in a for x in b)
counter = 0 
for i in range(0,len(Temp)):
    if(Temp[counter] in country): 
        Total_Cases.append(Temp[counter+1])
        New_Cases.append(Temp[counter+2])
        Total_Death.append(Temp[counter+3])
    counter = counter+1
    
#     print(info)
    #print(tag.string)
    # soupy = BeautifulSoup(str(i),'html.parser',store_line_numbers=True)
    # print(str(soupy.sourceline))
    
# soup = str(soup)
# line_number = soup.split('\n')
# if any():
    
    
    



# df = pd.DataFrame({'Country':country,'Price':prices,'Rating':ratings}) 
df = pd.DataFrame({'Country':country,'Total_Cases': Total_Cases,'New_Cases':New_Cases,'Total_Death':Total_Death }) 
df.to_csv('products.csv', index=False, encoding='utf-8')