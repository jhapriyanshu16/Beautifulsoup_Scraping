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
clg_location_list = []
clg_approval_list = []
clg_course_list = []
clg_cutoff_list = []
clg_fees_list = []
program_name_list = []
avg_pack_list = []
high_pack_list = []
clg_review_list = []
clg_tag_list = []
clg_ranking_list = []
ranking_out_of_list = []

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
            location = td.div.find('span',class_='jsx-3230181281 pr-1 location')
            if(location):
                clg_location_list.append(location.text.strip())
            else:
                clg_location_list.append('')
            approval = td.div.find('span',class_='jsx-3230181281 approvals pl-1')
            if(approval):
                clg_approval_list.append(approval.text.replace("\xa0"," ").strip())
            else:
                clg_approval_list.append('')
            course = td.div.find('span',class_='jsx-3230181281 course-name')
            if(course):
                clg_course_list.append(course.text.strip())
            else:
                clg_course_list.append('')
            cutoff = td.div.find('div',class_='jsx-3230181281 col-popular-course position-relative d-inline-flex justify-space-between mt-2').find('span',class_='jsx-3230181281').find_next_sibling('span')
            if(cutoff):
                clg_cutoff_list.append(cutoff.text.strip())
            else:
                clg_cutoff_list.append('')
        if(index == 2):
            fees = td.a.find('span',class_="jsx-3230181281 text-lg text-green d-block font-weight-bold mb-1")
            if(fees):
                clg_fees_list.append(int(fees.text[2:].replace(',','').strip()))
            else:
                clg_fees_list.append('')
            program = td.a.find('span',class_="jsx-3230181281 fee-shorm-form")
            if(program):
                program_name_list.append(program.text.strip())
            else:
                program_name_list.append('')
        if(index == 3):
            package = td.find_all('span',class_="jsx-914129990 text-green d-block mb-1")
            if (len(package)==2):
                avg = td.find_all('span',class_="jsx-914129990 text-green d-block mb-1")[0]
                if(avg):
                    avg_pack_list.append(int(avg.text[2:].replace(',','').strip()))
                else:
                    avg_pack_list.append('')
                high = td.find_all('span',class_="jsx-914129990 text-green d-block mb-1")[1]
                if(high):
                    high_pack_list.append(int(high.text[2:].replace(',','').strip()))
                else:
                    high_pack_list.append('')
            else:
                high = td.find_all('span',class_="jsx-914129990 text-green d-block mb-1")[0]
                if(high):
                    high_pack_list.append(int(high.text[2:].replace(',','').strip()))
                else:
                    high_pack_list.append('')
        if(index == 4):
            review = td.find('span',class_='jsx-3230181281 lr-key text-lg text-primary d-block font-weight-medium mb-1')
            if(review):
                clg_review_list.append(review.text.strip())
            else:
                clg_review_list.append('')
            tag = td.find('span',class_='jsx-3230181281 placement-reviews-back pointer position-relative p-1 tagline mt-2 font-weight-medium d-inline-flex align-items-center').find('span',class_='jsx-3230181281')
            if(tag):
                clg_tag_list.append(tag.text)
            else:
                clg_tag_list.append('')
        if(index == 5):
            ranking = td.find('span',class_='jsx-2794970405 rank-span no-break').find('span',class_='jsx-2794970405')
            if(ranking):
                clg_ranking_list.append(int(ranking.text.split('th')[0].replace('#', '')))
                ranking_out_of_list.append(int((ranking.find('span',class_='jsx-2794970405 text-primary').text)))
            else:
                clg_ranking_list.append('')
                ranking_out_of_list.append('')






print(rank_list)
print(clg_name_list)
print(clg_link_list)
print(clg_location_list)
print(clg_approval_list)
print(clg_course_list)
print(clg_cutoff_list)
print(clg_fees_list)
print(program_name_list)
print(avg_pack_list)
print(high_pack_list)
print(clg_review_list)
print(clg_tag_list)
print(clg_ranking_list)
print(ranking_out_of_list)

