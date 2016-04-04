#-*-coding:utf-8-*-
'''
Coding Just for Fun
Created by burness on 16/4/3.
'''
import re
import urllib2
from lxml import etree
def get_papers_link(html):
    page = etree.HTML(html.lower().decode('utf-8'))
    papers_hrefs = page.xpath(u"//h3/a")
    for href in papers_hrefs:
        a = href.attrib
        b = href.text
        print a['href']+' ,title:'+b



if __name__ == '__main__':
    # 利用xpath
    # rex = pdf_rex
    # proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
    # opener = urllib2.build_opener(proxy)
    # urllib2.install_opener(opener)
    page = urllib2.urlopen(urllib2.Request("https://scholar.google.com.hk/scholar?hl=zh-CN&q=nlp&btnG=&lr=",
                                           headers={"User-Agent":"Mozilla/5.0 Cheater/1.0"}))
    html=page.read()
    print 'read web page successfull!'
    result = get_papers_link(html)