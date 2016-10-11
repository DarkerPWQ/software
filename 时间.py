from time import time,sleep
a=time()
sleep(5)


print time()-a
while time()-a < 30:
    pass
print 'aaaa'
print time()-a