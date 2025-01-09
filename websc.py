# import requests
# import time
# from fake_useragent import UserAgent

# url = "https://www.flipkart.com/search?q=headsets&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

# session = requests.Session()

# headers = {
# 'User-Agent': UserAgent().random,
# 'Accept-Language': 'en-US,en;q=0.9',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Connection': 'keep-alive',
# 'Referer': 'https://www.google.com'
# }

# proxy_auth =  
# proxies = {
# 'http': f'http://{proxy_auth}',
# 'https': f'https://{proxy_auth}'
# }

# time.sleep(2)
# r = session.get(url,headers=headers,proxies=proxies)

# with open("file.html","w") as f:
#     f.write(r.text) 