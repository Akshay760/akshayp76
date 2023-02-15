#!/usr/bin/env python
# coding: utf-8

# In[133]:


from bs4 import BeautifulSoup
import requests


# In[134]:


page = requests.get('https://www.flipkart.com/cameras/dslr~type/pr?sid=jek%2Cp31&p%5B%5D=facets.brand%255B%255D%3DCanon&otracker=clp_pmu_v2_camera-clp-store_5ZEX38D1TJC6')
page


# In[135]:


soup=BeautifulSoup(page.content)
soup


# In[136]:


#scraping of title
first_title = soup.find('div',class_="_4rR01T")
first_title


# In[137]:


first_title.text


# In[138]:


#scraping of price
price = soup.find('div',class_="_30jeq3 _1_WHN1")
price.text


# In[139]:


#scraping of rating
rating= soup.find('span',class_='_2_R_DZ')
rating.text


# In[140]:


#scraping of multiple titles
titles=[]
for i in soup.find_all ('div',class_="_4rR01T"):
    titles.append(i.text)


# In[141]:


titles


# In[142]:


#scraping of multiple price
price = []
for i in soup.find_all ('div',class_="_30jeq3"):
    price.append(i.text)


# In[143]:


price


# In[144]:


rating=[]
for i in soup.find_all('span',class_='_2_R_DZ'):
    rating.append(i.text)


# In[145]:


rating


# In[146]:


#scraping of images
images = []
for i in soup.find_all("img",class_="_396cs4"):
    images.append(i.get('src'))


# In[147]:


images


# In[148]:


#printing lengths
print(len(titles),len(price),len(off),len(images))


# In[150]:


#making dataframe
import pandas as pd
df=pd.DataFrame({'titles':titles,'price':price,'rating':rating,'images':images})
df


# In[ ]:





# In[ ]:




