import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}
url = "https://collegedunia.com/india-colleges"
response = requests.get(url,headers=headers)

rank_list =[]
clg_name_list = []
clg_link_list = []

soup = BeautifulSoup(response.text,'html.parser')
table_wrapper = soup.find('div',class_= 'jsx-4033392124 jsx-1933831621 table-wrapper')
tr_list = table_wrapper.div.table.tbody.find_all('tr',recursive=False)
for tr in tr_list:
    td_list = tr.find_all('td',recursive=False)
    for index,td in enumerate(td_list):
        if (index==0):
            rank_list.append(int(td.text.lstrip('#')))
        if (index == 1):
            clg_name_list.append(td.div.div.a["data-csm-title"])
            clg_link_list.append(td.div.div.a["href"])
    # break

# print(rank_list)
# print(clg_name_list)
# print(clg_link_list)


