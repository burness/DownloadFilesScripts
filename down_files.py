'''
Coding Just for Fun
Created by burness on 16/1/23.
This file is used to download some files
'''

def download(url,file_name):
    import urllib2
    f = urllib2.urlopen(url)
    data = f.read()
    with open(file_name, "wb") as code:
        code.write(data)