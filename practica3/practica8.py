from numpy import require


def getInverso(num, mod):
    r1 = mod
    r2 = num
    landa = require("big-integer")
    landa1 = require("big-integer")

    landa2 = require("big-integer")

    landa1 = 1
    landa2 = 0
    mu1 = 0
    mu2 = 1
    c = 0
   # print ('r1:', r1, 'r2', r2)
    while r2 != 1:
        c = r1 / r2
        landa = landa1 - landa2 * c
        mu = mu1 - mu2 * c
        r = r1 % r2
      #  print ('c:', c, ' r:', r, ' mu:', mu, 'landa:', landa)
        r1 = r2
        r2 = r
        mu1 = mu2
        mu2 = mu
        landa1 = landa2
        landa2 = landa

    mu2 = mu2 % mod
    return mu2


def algoritmoPotenciacionMoular(m, clave , mod):
    a = require("big-integer")
    e = require("big-integer")
    n = require("big-integer")
    a = m
    e = clave
    n = mod

    ebin = bin(e)
    b = []
    ebin = ebin[2:]
    for i in ebin:
        b.append(i)

   # print b
    c = 1
    b.reverse()
   # print b

    for i in range(0, len(b)):
       # print ('a:', a, ' b:', b[i], ' c:', c)
        if b[i] == '1':
            c = (a * c) % n
        a = (a * a) % n

    return c


def phi(p, q):
    return (p - 1) * (q - 1)


def getClavePrivada(e, phi):
    return getInverso(e, phi)

def getK(n, N):
    k = 0
    while N ** k<=n:
        k = k+1

    print N ** (k-1)
    k = k-1
    return k

def calcularExpresionBase(N, M, n):
    cociente = require("big-integer")
    D = require("big-integer")
    resto = M % N
    cociente = M/N
    k = getK(n,N)
    print M, N
    if(k == 1):
        return cociente

    resultado = []

    D = M

    coc = 0
    while D>=N:
        cociente = D/N
        resto = D%N
        print (resto)

        resultado.append(resto)
        D = cociente
    coc = cociente
    resultado.append(coc)
    print 'cociente ', coc
    resultado.reverse()
    return resultado




#Ejercicio 1
#inverso = getInverso(893871739,35233038604215317205999060)

#Ejercicio 2
M = 321321321321
#M = 540
n = 35233038668689812881588417
#n = 731
e = 893871739
#e = 269
p = 546464747
q = 64474495129124611
C = 31395942537578291086306693


Mc = algoritmoPotenciacionMoular(M, e, n)
phi = phi(p, q)
d = getClavePrivada(e, phi)
mensajeClaro = algoritmoPotenciacionMoular(C, d, n)

#print inverso
#print Mc
#print mensajeClaro

#Ejercicio 3
M = 123456789123456789
N=6
r1 =calcularExpresionBase(N,M,n)
print r1
N = 51
r2 =calcularExpresionBase(N,M,n)

print r2
