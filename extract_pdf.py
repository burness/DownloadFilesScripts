'''
Coding Just for Fun
Created by burness on 16/1/23.
'''
import re
import urllib2
from down_files import download
from tqdm import *
from config import pdf_rex
def get_url(html,rex):
    alist = []
    r = re.compile(rex)
    matchs = r.findall(html)
    if matchs != None:
        for found in matchs:
            if found not in alist:
                if not re.match('^http',found):
                    alist.append('http://cs224d.stanford.edu/'+found)
                else:
                    alist.append(found)
    return alist

rex = pdf_rex
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
page=urllib2.urlopen('http://cs224d.stanford.edu/syllabus.html')
# page = urllib.urlopen('./stanford.html')
html=page.read()
page.close()

# print test(html,rex)
for url in tqdm(get_url(html,rex)):
    file_name = url.split('/')[-1]
    print file_name
    file_path = '/Users/burness/Documents/stanford nlp and dl/reading/'
    print 'downloading ', url
    try:
        download(url, file_path+file_name)
    except:
        print 'download %s error!!!'%url
        continue
    else:
        print 'download %s sucessful'%url