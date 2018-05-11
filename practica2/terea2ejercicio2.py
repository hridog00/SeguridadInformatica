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

def tablero(errores, H,q):
    #tablero = np.dot(np.squeeze(np.asarray(H)), np.squeeze(np.asarray(errores)))
    tablero = np.dot(H, errores)%q
    tablero = trasponerY(tablero)
    return tablero
def transpuesta(matriz):
    rows = len(matriz)
    cols = len(matriz[0])


    return [[matriz[j][i] for j in xrange(rows)] for i in xrange(cols)]

def matrizControl(matriz,q):
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
            aux.append(-(A[i][j])%q)
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
         #   print tablero[j], ' ', sindrome[i],' ', correcto
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

def getSindromes(H, y,q):

    yT = trasponerY(y)


    sindromes = np.dot(H, yT)
    sindromes = sindromes%q


    s = trasponerY(sindromes)

    return s

def getMensaje(y,e,q):
    res = []
    print len(y), ' ', len(e)
    for i in range (0, len(y)):

       list = map(operator.sub, y[i], e[i])

       print 'l', list
       for j in range(0,3):
           res.append(list[j]%q)
    return res

def getmensajeFuente(C):
    alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz:.,;¿¡!()?"
    print len(alf)
    res = ''
    for x in C:

        aux = ''
        for y in x:
            aux = aux + str(y)

        a = int(aux, 3)
        print aux,' ', a
        res = res + alf[a]


    return res
#DATOS DEL CODIGO
#A=[[1,1,1],[1,1,0],[1,0,1],[0,1,1]]
A=[[1,2,1,2,1,2,1,2],[1,1,2,0,1,1,2,2],[1,0,1,1,1,1,2,1]]
res =[]
re = []
q=3
G = getMatrizGeneradora(A)
print 'Generadora'
print G
H=  matrizControl(A,q)
print 'Matriz de control'
print H
#
generarPalabrasQuarias(q, len(A), res, re)
print 'Palabras quarias'
print res
d = distanciaMinima(G,res,q)
t = capacidadCorrectora(d)
print 'distancia de Humming ',d,' capacidad ',t
aux = []
generarPalabrasQuarias(q, 11, aux, re)

errores = getErrores(aux,t)
erroresT = trasponerY(errores)
tablero = tablero(erroresT,H,q)
print 'SINDROMES tablero ', len(tablero)
print tablero
print 'ERRORES ', len(errores)
print errores
print 'FIN'


modelo01_lista03=[1,1,0,0,1,1,2,0,0,0,1,0,1,1,2,1,0,1,2,2,1,0,2,2,0,1,1,0,0,1,2,1,1,1,1,0,0,0,1,0,0,1,2,2,1,1,1,0,0,1,0,0,1,2,2,1,2,0,1,0,0,1,1,0,0,2,0,2,2,1,0,1,1,1,1,2,1,2,0,0,2,1,2,1,2,1,2,1,2,1,1,0,0,1,0,0,1,2,2,0,0,1,0,1,1,2,0,0,0,1,2,1,1,0,1,0,2,0,2,1,2,2,0,0,1,2,1,2,1,2,1,2,2,1,2,0,1,1,2,0,0,0,1,0,0,1,0,0,1,0,0,1,2,2,2,1,2,0,1,1,2,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,2,2,1,0,2,0,1,1,2,0,0,0,1,2,0,1,1,0,1,1,1,1,2,1,1,0,2,2,2,2,0,2,0,0,0,2,1,0,2,0,0,2,2,0,0,1,0,2,2,2,0,2,2,2,2,1,2,1,2,1,2,2,2,0,2,0,0,0,2,1,1,1,0,0,1,1,0,0,2,2,2,0,2,1,2,1,2,1,2,1,0,1,2,2,1,0,1,2,2,1,0,1,1,1,2,2,2,0,2,0,0,0,0,0,0,2,2,2,0,2,0,0,0,2,1,0,0,2,1,1,0,2,1,0,2,1,1,2,1,0,1,2,2,1,0,2,2,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,2,1,1,0,0,0,1,1,2,0,1,1,2,2,1,0,1,2,2,2,0,2,0,0,0,2,0,1,1,2,1,2,1,2,1,2,1,1,2,1,0,2,1,1,2,1,0,0,2,1,0,2,2,1,0,0,0,2,0,2,1,1,0,1,1,1,1,2,1,0,1,1,2,1,0,1,2,2,1,0,2,0,0,1,2,1,2,1,2,1,2,0,1,1,2,1,0,1,2,2,1,0,2,0,2,2,2,2,0,2,0,0,0,2,2,1,1,1,0,0,1,2,1,1,0,2,0,1,2,1,2,1,2,1,2,2,0,1,0,2,2,1,0,0,0,2,0,0,2,1,0,1,1,1,1,2,1,2,1,0,2,1,0,1,2,2,1,0,2,0,0,1,2,1,2,1,2,1,2,1,2,2,1,2,1,2,1,2,1,2,2,0,2,0,1,0,2,0,2,1,2,1,2,0,1,1,0,0,1,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,2,1,2,1,2,0,0,2,2,0,2,2,2,2,1,2,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,2,0,1,0,1,2,1,2,2,1,0,2,2,1,0,0,0,2,1,0,0,1,0,1,1,1,1,2,1,1,2,2,1,1,0,0,1,2,1,1,0,2,0,1,2,1,2,1,2,1,2,0,2,1,1,2,0,2,1,1,2,0,1,1,0,2,0,0,2,2,0,0,1,0,0,0,0,0,0,0,0,0,0,0,2,1,2,1,0,2,1,1,2,1,0,1,0,0,1,2,1,2,1,2,1,2,0,0,0,2,2,2,0,2,0,0,0,1,2,0,0,1,2,2,0,1,2,0,2,2,2,2,2,0,0,2,1,2,2,2,1,2,2,1,0,1,2,2,1,0,2,1,2,2,0,2,2,2,2,1,2,1,0,0,0,0,0,0,0,0,0,0,1,0,0,2,2,2,0,2,0,0,0]

y = dividirEnY(modelo01_lista03,11)

cola = []
if len(y[len(y)-1])<11:
    cola.append(y.pop())

sindromes = getSindromes(H, y,q)
print 'SINDROMES ',len(sindromes)
print sindromes

erroresY = encontrarErroresTablero(sindromes,tablero,errores)
print 'Y'
print y

print 'ERRORES PATRON'
print erroresY
print len(erroresY)
dec = getMensaje(y,erroresY,q)
for i in cola:
    for j in i:

        dec.append(j)

print 'dec', dec
c = dividirEnY(dec,4)


print 'lista', c
res = getmensajeFuente(c)
print res











