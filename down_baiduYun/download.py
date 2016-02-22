'''
Coding Just for Fun
Created by burness on 16/2/4.
'''
import urllib2

# TODO: 实现断点续传
#  header传一个下载的存储的值

request_header = {"referer":"http://pan.baidu.com/s/1nuepR0d"}
# opener = urllib2.build_opener(request_header)
# urllib2.install_opener(opener)
req = urllib2.Request("http://www.baidupcs.com/rest/2.0/pcs/file?method=batchdownload&app_id=250528&zipcontent=%7B%22fs_id%22%3A%5B718118434897580%5D%7D&sign=DCb740ccc5511e5e8fedcff06b081203:A47Z2PHFiLoBgy6TZcdRZk%2F7p0A%3D&uid=1730478110&time=1454600654&dp-logid=788302039593798281&dp-callid=0",headers=request_header)
k_unit = 1024
m_unit = k_unit**2
g_unit = k_unit**3
t_unit = k_unit**4
u = urllib2.urlopen(req)
f = open('test.zip','wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print 'the file size : %f g'% (file_size*1.0/(g_unit))
file_size_dl = 0
block_sz = m_unit
while True:
    # 每次到一定大小时就会出现之后一直卡住的问题,应该是read次数太多的问题吧,增加block_sz的大小来试下
    buffer = u.read(block_sz)
    if not buffer:
        break
    file_size_dl += block_sz
    f.write(buffer)
    status = r"%10d m [%3.2f%%]" % (file_size_dl/m_unit, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status

f.close()
