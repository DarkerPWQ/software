# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
f=open('tianqi6.txt','r+')
print '2'
l={}
for i in range(2587):
    b=f.readline()
    b=b.replace('\n','')
    print unicode(b[9:])
    l[unicode(b[9:])]=b[0:9]
    print unicode(b[9:])
print 'ok'
f.close()
print l
if unicode('南京')in l:
    print 'zai'