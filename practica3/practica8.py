def getInverso(num, mod):
    r1 = mod
    r2 = num
    landa1 = 1
    landa2 = 0
    mu1 = 0
    mu2 =1
    c = 0
    print ('r1:',r1, 'r2',r2)
    while r2 != 1:
        c = r1/r2
        landa = landa1 - landa2*c
        mu = mu1 - mu2*c
        r = r1 % r2
        print ('c:',c,' r:',r,' mu:',mu, 'landa:',landa)
        r1 = r2
        r2 = r
        mu1 = mu2
        mu2 = mu
        landa1 = landa2
        landa2 = landa

    mu2 = mu2%mod
    return mu2

def algoritmoPotenciacionMoular(a,e,n):
    ebin = bin(e)
    b = []
    ebin =  ebin[2:]
    for i in ebin:
        b.append(i)

    print b
    c = 1
    b.reverse()
    print b

    for i in range(0,len(b)):
        print ('a:',a,' b:',b[i], ' c:',c)
        if b[i]=='1':
            c =(a*c)%n
        a = (a*a)%n

    return c


#inverso = getInverso(893871739,35233038604215317205999060)

M =321321321321
n=35233038604215317205999060
e=893871739

Mc = algoritmoPotenciacionMoular(M,e,n)
print Mc