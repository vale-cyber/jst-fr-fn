#!/usr/bin/env python
# coding: utf-8

# In[2]:


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
# opens a connection
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html parser 
page_soup = soup(page_html, "html.parser")
#Grabs each product/ use findAll command to get specific info
containers = page_soup.findAll("div",{"class":"item-container"})

out_filename = "Graphics_cards.csv"

headers = "brand,product_name,shipping \n"

f = open(out_filename, "w")
f.write(headers)

make = containers[0].find("div","item-info")

for make in containers:
    
    brand = make.findAll("div", {"class": "item-branding"})[0].a.img["title"]
    
    description = make.findAll("a", {"class": "item-title"})[0].text
    
    shipping = make.findAll("li",{"class":"price-current"})[0].text.strip()
    
    Price = make.findAll("li",{"class":"price-current"})[0].text.strip(' \xa0\r\n            \n–\n\n')
    
    print("Brand:" + brand)
    print("Description:" + description)
    print("Shipping:" + shipping)
    print("Price:" + Price)
    f.write(brand + ", " + description.replace(",", "|") + "," + shipping + "\n")
    
f.close()

print(make)


# In[1]:





# In[ ]:




