import requests

url = "https://www.scrapethissite.com/pages/forms/?page_num=1"
response = requests.get(url)
print(response.text)