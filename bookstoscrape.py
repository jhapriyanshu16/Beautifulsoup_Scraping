import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/index.html"

response = requests.get(url)

with open ('booksfile.html','w') as html:
    html.write(response.text)

with open ('booksfile.html','r') as fp:
    soup = BeautifulSoup(fp,'html.parser')

#    # print(soup.title)
#    title_text = soup.title.text.strip()
#    # print(title_text)
#    print(soup.a) #This gives the first anchor tag
#    print(soup.find('a')) #same as print(soup.a)

#Here the anchor tag we want to target is inside an article tag with class product_pod
# print(soup.find('article'))
#print(soup.find('article',class_ = 'product_pod')) #Gives article tags where class in product_pod
# link = soup.find('article',class_ = 'product_pod').h3.a
# print(link.text) #prints the text of the link
# print(link["title"]) #prints the title
# print(link["href"]) #prints the actual link

articleTagsWithClassProduct_pod = soup.find_all('article',class_ = 'product_pod')
for elem in articleTagsWithClassProduct_pod:
    #print(elem.h3.a["title"]) #Returns every book title
    pass

divWithClassproduct_price = soup.find_all('div',class_ = 'product_price')
for elem in divWithClassproduct_price:
    price = elem.p.text
    price_without_curr_sym = float(price.strip('Â£'))
    #print(price_without_curr_sym)    #Returns every price
    pass



#Storing and mapping Book title and price
product_pod_list = soup.find_all('article',class_ = 'product_pod')
data = []
for elem in product_pod_list : 
    title = elem.h3.a["title"]
    price = float((elem.find('div',class_ = 'product_price').p.text).lstrip('Â£'))
    data.append({title:price})

print(data)




    













