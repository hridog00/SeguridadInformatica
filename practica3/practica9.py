# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
from random import randrange, random
import sympy as sy
import binary as binary
from numpy import require

import random

def getInverso(num, mod):
    r1 = mod
    r2 = num
    landa = require("big-integer")
    landa1 = require("big-integer")

    landa2 = require("big-integer")
    mu2 = require("big-integer")
    landa1 = 1
    landa2 = 0
    mu1 = 0
    mu2 = 1
    c = 0
    # print ('r1:', r1, 'r2', r2)
    while r2 != 1:
        print (r1, r2)
        c = r1 // r2
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


def algoritmoPotenciacionMoular(m, clave, mod):
    a = require("big-integer")
    e = require("big-integer")
    n = require("big-integer")
    e = require("big-integer")
    a = m
    e = clave
    n = mod

    ebin = bin(int(e))
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
    while N ** k <= n:
        k = k + 1

    k = k - 1
    return k


def calcularExpresionBase(N, M, n):
    cociente = require("big-integer")
    D = require("big-integer")
    resto = require("big-integer")
    resto = M % N
    cociente = M // N
    resultado = []
    D = M
    coc = 0
    while D > N:
        cociente = D // N
        resto = D % N
        resultado.append(resto)
        D = cociente

    coc = cociente
    resultado.append(coc)
    resultado.reverse()
    return resultado


def pasarNumerico(msg, alf):
    resultado = []
    for i in msg:
        resultado.append(alf.find(i))
    return resultado

def getBloquesCifrar(k, C):
    print(len(C))
    result = []
    i = 0
    while i < len(C):
        aux = []
        for j in range(0, k):
            aux.append(C[i + j])

        i = i + k
        print (aux)
        result.append(aux)
    return result

def getBloques(k, C):
    result = []
    i = 0
    while i < len(C):
        aux = []
        for j in range(0, k + 1):
            aux.append(C[i + j])

        i = i + k + 1
        result.append(aux)
    return result


def getC(bloque, k, N):
    print (bloque)
    c = require("big-integer")
    c = 0
    exp = k
    for i in range(0, k+1):
        a = require("big-integer")
        a = (N ** exp)
        c = c + bloque[i] * a
        exp = exp - 1


    return c
def getCCifrar(bloque, k, N):
    print (bloque)
    c = require("big-integer")
    c = 0
    exp = k-1
    for i in range(0, k):
        print(exp)
        a = require("big-integer")
        a = (N ** exp)
        c = c + bloque[i] * a
        exp = exp - 1


    return c

def devolerLetras(alf, m):
    msg = ""
    for i in m:
        msg = msg + alf[i]
    return msg


def encriptar(texto, n, e):
    alf = "abcdefghijklmn�opqrstuvwxyzABCDEFGHIJKLMN�OPQRSTUVWXYZ����������0123456789 ,.:;-�?()"

    # alf = "ABCDEFGHIJKLMNNOPQRSTUVWXYZ"


    #n=731
    #e=269
    N = len(alf)
    print (len(texto))
    k = getK(n, N)
    print ('k',k)
    while ((len(texto) % k) != 0):

        texto = texto + " "

    print('long',len(texto))

    M = pasarNumerico(texto, alf)
    C = getBloquesCifrar(k, M)
    print (C)
    res = ""
    for i in C:
        c = getCCifrar(i, k, N)
        print ('c:', c)
        m = algoritmoPotenciacionMoular(c, e, n)
        print ('m:', m)
        numeros = calcularExpresionBase(N, m, n)
        while(len(numeros)<k+1):
            numeros = [0] + numeros
        print ('numeros:', numeros)
        msg = devolerLetras(alf, numeros)
        #   print (msg)
        res = res + msg
    print (res)
    return res

def desencriptar(msg,n,e,phi):
    alf = "abcdefghijklmn�opqrstuvwxyzABCDEFGHIJKLMN�OPQRSTUVWXYZ����������0123456789 ,.:;-�?()"
    #alf = "ABCDEFGHIJKLMNNOPQRSTUVWXYZ"

    N = len(alf)
    M = pasarNumerico(msg, alf)
    k = getK(n, N)
    d = getClavePrivada(e, phi)
    print ('len y k ',len(msg),  k)
    C = getBloques(k, M)

    res = ""
    for i in C:
        c = getC(i, k, N)
     #   print ('c:', c)
        m = algoritmoPotenciacionMoular(c, d, n)
      #  print ('m:', m)
        numeros = calcularExpresionBase(N, m, n)
     #   print ('numeros:')
      #  print (numeros)
        msg = devolerLetras(alf, numeros)
     #   print (msg)
        res = res + msg

    return res

def primosEntreSi(phi):
    result = []

    for i in range(1,phi-1):

        if mcd(i,phi) == 1:
            result.append(i)


    return result

def mcd(a, b):
    resto = 0
    while(b > 0):
        resto = b
        b = a % b
        a = resto
    return a




def generarClavePublica():
    p = sy.randprime(50, 50000)
    q= sy.randprime(50,50000)

    n = p*q
    phi = ((p-1)*(q-1))
    print (phi)
    e = random.choice(primosEntreSi(phi))
    print ('p:', p, 'q:', q, 'n:', n, 'phi:', phi, 'e:', e)
    print('E', e, 'N', n)
    clave = []
    clave.append(n)
    clave.append(e)
    clave.append(phi)

    return clave
nB = 743330222539755158153
eB = 80263681
pB = 27264083009
qB = 27264083017
phi = (pB-1)*( qB - 1)

#msg = "ya que, m�s que gorda, era una falsa delgada.   "
msg = "Hola esto es una prueba muy interesante."
claves = generarClavePublica()
#nB = claves[0]
#eB = claves[1]
#phi = claves[2]

#nB = 5244938048376303456108649
#eB = 114340249
#pB = 2290182972661
#qB = 2290182972709
#phi = (pB-1)*( qB - 1)
print ('n:',nB, 'eB:', eB, 'phi:', phi)

text = encriptar(msg,nB,eB)
print ('encripto:',text)
#
# #msg = "AIDAVCANH"
alf = "abcdefghijklmn�opqrstuvwxyzABCDEFGHIJKLMN�OPQRSTUVWXYZ����������0123456789 ,.:;-�?()"
alf = "ABCDEFGHIJKLMNNOPQRSTUVWXYZ"
N = len(alf)
# var = 0
#
msg = "q��usynX�p3h7k�2 M.S�NYi�:c0�hS39X.8Y0�tb���WDaJ8 x."
#msg = "p,6BNVtAXlGlC3uFv?�?hAo��S�tuKOAUtKEM74zTpKVDXIh�A7�xcOg7Yo78P�q5l"
# #msg = "AIDAVCANH"
#
msg
M = pasarNumerico(msg, alf)
#
k = getK(nB, N)
# print ('k:',k)
# #
# # nB = 2641
# # eB =497
# # k=2
#phi = (pB-1)*( qB - 1)
#
print ('Aqui:',desencriptar(text, nB, eB, phi))

print ('n:',nB, 'eB:', eB, 'phi:', phi)
