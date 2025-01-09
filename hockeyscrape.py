import requests
from bs4 import BeautifulSoup
import pandas as pd

scraped_data = {"Team Name":[],"Year":[],"Wins":[],"Losses":[],"Goals For (GF)":[],"Goals Against (GA)":[]}

for i in range (1,25):
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    matches = soup.find_all('tr',class_='team')

    for match in matches:
        name = match.find('td',class_="name").text.strip()
        scraped_data.get("Team Name").append(name)
        year = int(match.find('td',class_="year").text.strip())
        scraped_data.get("Year").append(year)
        wins = int(match.find('td',class_="wins").text.strip())
        scraped_data.get("Wins").append(wins)
        losses = int(match.find('td',class_="losses").text.strip())
        scraped_data.get("Losses").append(losses)
        gf = int(match.find('td',class_="gf").text.strip())
        scraped_data.get("Goals For (GF)").append(gf)
        ga = int(match.find('td',class_="ga").text.strip())
        scraped_data.get("Goals Against (GA)").append(ga)




df = pd.DataFrame(scraped_data)
df.to_excel('hockeydata.xlsx',index=False)
print("Done Boss")