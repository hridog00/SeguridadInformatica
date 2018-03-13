len = ''

variable = 0
for x in range(0, 120):
    if x<10:
         len = 'a00' + str(x)
    else:
        if x < 100:
            len = 'a0' + str(x)
        else:
            len = 'a'+str(x)
    print len

print len[:2]
