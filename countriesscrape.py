import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)

with open('countrieshtml.html','w',encoding='utf-8') as file:
    file.write(response.text)

with open("countrieshtml.html","r") as file:
    soup = BeautifulSoup(file,'html.parser')


country_info_list = soup.find_all('div',class_="col-md-4 country")

country_list = []
capital_list = []
population_list = []
area_list = []


for elem in country_info_list:
    name = elem.h3.text.strip()
    capital = elem.find('div',class_ = "country-info").find('span',class_= "country-capital").text.strip()
    population = int(elem.find('div',class_ = "country-info").find('span',class_= "country-population").text.strip())
    area = float(elem.find('div',class_ = "country-info").find('span',class_= "country-area").text.strip())
    
    country_list.append(name)
    capital_list.append(capital)
    area_list.append(area)
    population_list.append(population)


data = {
    "Country": country_list,
    "Capital": capital_list,
    "Population": population_list,
    "Area" : area_list
}


df = pd.DataFrame(data)

df.to_excel("countries_scraped_data.xlsx", index=True)

print("Done Boss")