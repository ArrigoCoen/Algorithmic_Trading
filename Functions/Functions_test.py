#%%
# Similar problem
# https://stackoverflow.com/questions/61724392/how-to-scrape-all-rows-from-a-dynamic-table-in-html-using-python

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
from Project_Functions import *


#%%
test_my_print()


#%%



#%%
def extract():
    url = 'https://stockanalysis.com/stocks/'
    headers = {'User-Agent': ' user agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
    r = requests.get(url,headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

soup = extract()

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

url = 'https://stockanalysis.com/stocks/'
headers = {'User-Agent': ' user agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
r = requests.get(url,headers)

# The next line should be 200 to check that we are extracting correctly the web page info
print(r.status_code)


soup = BeautifulSoup(r.text, 'html.parser')

# print(soup)
league_table = soup.find('table', class_ = 'symbol-table index')

print(league_table)

#%%



col_df = ['Symbol', 'Company_name', 'Industry', 'Market_Cap']

df = pd.DataFrame(np.zeros([8000, len(col_df)]))
df.columns = col_df
i = 1

for team in league_table.find_all('tbody'):
    # i = 1
    rows = team.find_all('tr')
    print('rows ler =', len(rows))
    for i, row in enumerate(rows):
        print(i)
        s_symbol = row.find_all('td')[0].text
        s_company_name = row.find_all('td')[1].text
        s_industry = row.find_all('td')[2].text
        s_market_cap = row.find_all('td')[3].text
        df.iloc[i] = [s_symbol, s_company_name, s_industry, s_market_cap]
        # if i < 20:
        #     print(s_company_name)
        #     i = i + 1

#%%
df.tail()

#%%
df.head()

/html/body/div[1]/div[2]/main/div/div/div[2]/table/tbody/tr[3496]/td[1]/a

#%%
len(rows)

#%%
sum(df['Symbol'] != 0)

#%%
len(league_table.find_all('tbody'))

#%%
# From
# https://www.youtube.com/watch?v=LSysb73avyw
import requests
import lxml.html


url = 'https://stockanalysis.com/stocks/'
html = requests.get(url)
doc = lxml.html.fromstring(html.content)
print(html.content)
#%%

list_stocks = doc.xpath('/html/body/div[1]/div[2]/main/div/div/div[2]/table/tbody/tr[*]/td[1]/a/text()')

print(list_stocks)
print(len(list_stocks))

#%%


list_stocks = doc.xpath('/html/body/div[*]/div[*]/main/div/div/div[*]/table/tbody/tr[*]/td[*]/*/text()')
print(list_stocks)

#%%



my_xpath = '//*[@id="symbol-table"]/tbody/tr[*]/td[*]/*/text()'
# my_xpath = '//*[@id="symbol-table"]/tbody/tr[*]/td[2]'
list_stocks = doc.xpath(my_xpath)
print(list_stocks)


#%%
len(list_stocks)


#%%



#%%


# Importing libraries
import numpy as np  # numerical computing library
import pandas as pd # panel data library
import requests     # http requests library
from bs4 import BeautifulSoup


url = 'https://stockanalysis.com/stocks/'
headers = {'User-Agent': ' user agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
r = requests.get(url, headers)
soup = BeautifulSoup(r.text, 'html')
league_table = soup.find('table', class_ = 'symbol-table index')
col_df = ['Symbol', 'Company_name', 'Industry', 'Market_Cap']

for team in league_table.find_all('tbody'):
    # i = 1
    rows = team.find_all('tr')
    df = pd.DataFrame(np.zeros([len(rows), len(col_df)]))
    df.columns = col_df
    for i, row in enumerate(rows):
        s_symbol = row.find_all('td')[0].text
        s_company_name = row.find_all('td')[1].text
        s_industry = row.find_all('td')[2].text
        s_market_cap = row.find_all('td')[3].text
        df.iloc[i] = [s_symbol, s_company_name, s_industry, s_market_cap]

len(df)

#%%
df.tail()


#%%
sum(df['Symbol'] != 0)



#%%
def main(url):
    for item in range(1, 4):
        df = pd.read_html(url.format(item))[1]
        print(df)


main("http://5000best.com/websites/Games/{}/")


#%%

url = 'https://stockanalysis.com/stocks/'
item = 1
df = pd.read_html(url.format(item))[1]
#%%


#%%
#  WORKS LIKE A CHARM!!!!
import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd

url = 'https://stockanalysis.com/stocks/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
jsonStr = str(soup.find('script', {'id':'__NEXT_DATA__'}))

jsonStr = re.search('({.*})', jsonStr).group(0)
jsonData = json.loads(jsonStr)

df = pd.DataFrame(jsonData['props']['pageProps']['stocks'])
#%%
df.tail()

#%%
df.columns

#%%


#%%



