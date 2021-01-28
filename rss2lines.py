
# coding: utf-8

# In[1]:

import nltk, re, pprint
from nltk import word_tokenize


# In[1]:

#path = '/mnt/dee/Downloads/s.f/8089759_xml_2015_09_13_8f09c.xml'
#path = '/home/martin/Downloads/1997 LETTER TO SHAREHOLDERS_2015_09_02_6e847 (copy).xml'
#/home/martin/Downloads/tr-cduvozmezera-~uvoz.xml
#path = '/home/martin/Downloads/tr.xml'
path = '/home/martin/Dropbox/dis-DIIGO.g6/2017_04_08-bez-cntrl.xml'

from bs4 import BeautifulSoup, CData
 
soup = BeautifulSoup(open(path,'r'),  'xml')
 


import html.parser
html_parser = html.parser.HTMLParser()


# In[2]:

#soup
# on to xml s spatnumi byty asi vubec nenatahl


# In[3]:

###for cd in soup.findAll(text=True):
  ###if isinstance(cd, CData):
    
#cdatalist = [
#]

textl=[
    #x.find('link').string + ' en ' +
    x.find('link').string + '  ' +
    x.find('title').string+ '  ' +
    BeautifulSoup(
        html_parser.unescape(
            x.find('description').string
        )
    ).get_text()
    for x in soup.findAll('item')
]


# In[4]:

#textl


# In[ ]:




# In[5]:

linelist = [ " ".join(s.split())
 for s in textl
]


# In[6]:

with open("rss2lines,h4a.lines.txt", "w") as f:
    for line in linelist:
        print(line, file=f)# line file


# In[7]:

r = " ".join(linelist)


# In[8]:

# with open("file.txt", "w") as f: f.write(soup.prettify().encode('utf8'))
####type(raw)


# In[9]:

#import string


# In[10]:

tokens = word_tokenize(r.lower())
#print(raw)
#print(tokens)
#%history


# In[20]:

sst=sorted(set(tokens))


# In[21]:

print(len(sst))
len(tokens)


# In[22]:

text = nltk.Text(tokens)


# In[23]:

text.collocations(num=100)


# In[ ]:




# In[7]:

from nltk.book import *
fdist1 = FreqDist(text) 
print(fdist1) 

fdist1.most_common(50) 


# In[8]:

text5=text
fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 9 and fdist5[w] > 7)


# In[ ]:

#>>> import feedparser


# In[13]:

#>>> llog = feedparser.parse("file:///mnt/dee/Downloads/s.f/8089759_xml_2015_07_22_b841c.xml")


# In[14]:

#>>> len(llog.entries)


# In[63]:

#e=llog.entries[0]
get_ipython().magic('psearch e.v*')
get_ipython().magic('pinfo e.description')
#dir(e)


# In[64]:

#>>> import logging
#>>> logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# In[28]:


#from lxml import etree
#from lxml.html import parse
#with open(path, 'rb') as f:
 #   tree = etree.parse(f)


# In[58]:


#doc = tree.getroot()

#links = doc.findall(".//title")


# In[47]:

#soup.findAll('item')
#soup
with open("out.xml", "w") as fw:
    fw.write(soup.prettify())


# In[ ]:




# In[33]:

get_ipython().magic('pinfo soup.findAll')


# In[ ]:




# In[43]:

#print( ' %r' % y)
#print(type(y.string))

#print(unescaped)
y.string = u

