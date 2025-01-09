import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.espncricinfo.com/records/year/batting-most-runs-career/2024-2024/twenty20-internationals-3"
response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')
data_table = soup.find('table',class_="ds-table-xs").tbody.find_all('tr')

scraped_data = []
name_list = []
for i in range(0,len(data_table)):
    row = []
    name_list.append(data_table[i].find('td',class_="ds-min-w-max").span.a["title"])
    td_lst = data_table[i].find_all('td',class_="ds-min-w-max ds-text-right")
    for td in td_lst:
        row.append(td.text)
        
    scraped_data.append(row)


column_name = ["Span","Mat","Inns","NO","Runs","HS","Ave","BF","SR","100","50","0","4s","6s"]
df = pd.DataFrame(scraped_data,columns=column_name)
df.insert(0,"Player",name_list)
df.to_excel("Most_runs_in_2024(T20Is).xlsx",index=False)
print("Done")
