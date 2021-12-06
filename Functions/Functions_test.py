#%%


# Importing libraries
import numpy as np  # numerical computing library
import pandas as pd # panel data library
import requests     # http requests library
import xlsxwriter   # Excel documents writing library
import math         # mathematical functions library

from bs4 import BeautifulSoup


#%%
import os
os.getcwd()

#%%
def extract():
    url = 'https://stockanalysis.com/stocks/'
    headers = {'User-Agent': ' user agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
    r = requests.get(url,headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


#%%

# def transform(soup):

divs = soup.find_all('div', class_='overflow-x-auto')



#%%

#  [here](https://www.youtube.com/watch?v=PPcgtx0sI2E&list=PLOxtsYaYauiSoHSyjo4uUZhnaWjNYdGfL&index=5&t=169s)

divs = soup.find_all('div', class_='overflow-x-auto')
divs = soup.find_all('div', class_='symbol-table index')
aca = 1
for item in divs:
    print(aca)
    title = item.find('a')
    print(title)
    aca = aca +1

#%%

soup


#%%




#%%