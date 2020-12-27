# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
from selenium.webdriver.chrome.options import Options 


def csvGenerator():

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome("Please insert chrome driver directory here",options=options)

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
    