td_list = section.tbody.find_all('td',class_= 'jsx-3230181281 font-weight-medium text-lg position-relative')
for td in td_list:
    print(td.text)