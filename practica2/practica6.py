# -*- coding: cp1252 -*-

import numpy as np
import operator

def errorPatron():

    return
def getMatrizGeneradora(A):

    id = []
    for i in range(0, len(A)):
        aux = []
        for j in range(0, len(A)):
            if i==j:
                aux.append(1)
            else:
                aux.append(0)
        id.append(aux)



    matriz = []
    for i in range(0, len(A)):
        aux = []
        for j in range (0, len(id[i])):
            aux.append(id[i][j])
        for j in range (0, len(A[i])):
            aux.append(A[i][j])
        matriz.append(aux)

    return matriz
def generarPalabrasQuarias(q, k, res, re):
    a = len(re)
    if a < k:
        for i in range(0, q):
            aux = []

            aux = re[:]
            aux.append(i)

            generarPalabrasQuarias(q, k, res, aux)

    else:
        res.append(re)




    return

def getErrores(error,t):
    res =[]

    for i in range(0, len(error)):
        aux = 0
        for j in range(0, len(error[i])):

            if error[i][j] != 0:
                aux = aux + 1

        if aux <= t:
            res.append(error[i])
    return res

def tablero(errores, H):
    #tablero = np.dot(np.squeeze(np.asarray(H)), np.squeeze(np.asarray(errores)))
    tablero = np.dot(H, errores)
    tablero = trasponerY(tablero)
    return tablero
def transpuesta(matriz):
    rows = len(matriz)
    cols = len(matriz[0])


    return [[matriz[j][i] for j in xrange(rows)] for i in xrange(cols)]

def matrizControl(matriz):
    A = transpuesta(matriz)
    id = []
    for i in range(0, len(A)):
        aux = []
        for j in range(0, len(A)):
            if i == j:
                aux.append(1)
            else:
                aux.append(0)
        id.append(aux)

    matriz = []
    for i in range(0, len(A)):
        aux = []
        for j in range(0, len(A[i])):
            aux.append(A[i][j])
        for j in range(0, len(id[i])):
            aux.append(id[i][j])

        matriz.append(aux)

    return matriz

def distanciaMinima(G, P,q):

    v = np.dot(P,G)
    res = v%q


    min = 100000000000
    for i in range(0, len(res)):
        aux = 0
        for j in range(0, len(res[i])):

            if res[i][j] != 0:
                aux = aux + 1

        if aux < min:
            if aux != 0:
                min = aux

    return min

def capacidadCorrectora(d):
    t = 0
    t = (d-1)/2
    return t

def dividirEnY(lista, num):
    y = []
    suma = 0
    for i in range(0, len(lista)):
        if suma >= len(lista):
            break
        elif suma + num >= len(lista):
            resA = []
            resA = lista[suma:]


            y.append(resA)
            break
        else:
            resA = []
            resA = lista[suma:suma + num]
            suma = suma + num
            y.append(resA)

    return y

def encontrarErroresTablero(sindrome,tablero, errores):
    erroresFinal=[]
    for i in range(0, len(sindrome)):
        index = 0
        for j in range(0, len(tablero)):
            correcto = 1
            for k in range (0, len(tablero[j])):
                if tablero[j][k] != sindrome[i][k]:
                    correcto=0
                    break
            if correcto==1:
                index = j
                erroresFinal.append(errores[index])
                break

    return erroresFinal

def trasponerY(y):
    yT = np.random.randint(0,1,(len(y[0]), len(y)))
    for i in range(0, len(y)):
        for j in range(0,len(y[0])):
            yT[j][i] = y[i][j]
    return yT

def getSindromes(H, y):

    yT = trasponerY(y)


    sindromes = np.dot(H, yT)
    sindromes = sindromes%2


    s = trasponerY(sindromes)

    return s

def getMensaje(y,e):
    res = []
    print len(y), ' ', len(e)
    for i in range (0, len(y)):

       list = map(operator.sub, y[i], e[i])
       print 'l', list
       for j in range(0,4):
           res.append(list[j]%2)
    return res

def getmensajeFuente(C):
    alf = "abcdefghijklmnopqrstuvwwyzABCDEFGHIJKLMNOPQRSTUVWXYZ :.,;��!"
    print len(alf)
    res = ''
    for x in C:

        aux = ''
        for y in x:
            aux = aux + str(y)

        a = int(aux, 2)
        print aux,' ', a
        res = res + alf[a]


    return res
#DATOS DEL CODIGO
A=[[1,1,1],[1,1,0],[1,0,1],[0,1,1]]
res =[]
re = []
q=2
G = getMatrizGeneradora(A)
print 'Generadora'
print G
H=  matrizControl(A)
print 'Matriz de control'
print H
#
generarPalabrasQuarias(q, len(A), res, re)
d = distanciaMinima(G,res,q)
t = capacidadCorrectora(d)
print 'distancia de Humming ',d,' capacidad ',t
aux = []
generarPalabrasQuarias(q, 7, aux, re)

errores = getErrores(aux,t)
erroresT = trasponerY(errores)
tablero = tablero(erroresT,H)
print 'SINDROMES'
print tablero
print 'ERRORES'
print errores
print 'FIN'

lista=[1,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,
0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,0,1,
0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1,1,
0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,
0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1,0,
0,0,0,0,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1,
1,1,1,0,0,1,1,0,0,1,1,0,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,
1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,
1,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,0,
0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,0,0,1,1,1,0,0,1,1,0,1,1,
0,0,0,1,0,0,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,1,1,0,
1,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,
0,0,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,0,1,0,1,1,0,0,1,1,1,0,
1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,
0,1,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,1,1,1,0,1,0,1,0,1,
0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0,0,1,
1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,
0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,1,
0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,
0,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,
0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1,0,1,0,
1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,0,1,1,0,0,0,1,
1,1,0,0,1,1,0,1,1,0,1,0,1,1,1,1,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,0,0,
1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,1,
0,0,1,1,0,0,0,0,1,1,0,1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,1,0,1,1,0,0,
1,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,
0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,
0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,
1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,1,0,0,1,1,1,1,0,0,0,0,
1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,0,0,
0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,1,0,0,1,
0,1,0,1,1,1,0,0,1,0,1,1,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1,
1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,1,1,1,0,1,
0,1,0,1,0,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,
0,0,1,1,1,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,
0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1,
1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,1,1,1,0,1,0,
0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,0,1,0,1,1,1,0,0,1,0,1,0,1,0,1,1,
0,0,1,0,1,0,1,0]

y = dividirEnY(lista,7)

cola = []
if len(y[len(y)-1])<7:
    cola.append(y.pop())

sindromes = getSindromes(H, y)

erroresY = encontrarErroresTablero(sindromes,tablero,errores)
print 'Y'
print y
print 'SINDROMES'
print sindromes
print 'ERRORES PATRON'
print erroresY
dec = getMensaje(y,erroresY)
for i in cola:
    for j in i:

        dec.append(j)

print 'dec', dec
c = dividirEnY(dec,6)


print 'lista', c
res = getmensajeFuente(c)
print res










