# -*- coding: cp1252 -*-

import numpy as np
import operator

def getMensajeLineal(A):
    resultado = []
    suma = 0
    for i in range(0,len(A)):
        print len(A), ' ', suma
        if suma>=len(A):

            break
        elif suma+12>=len(A):
            print 'Entro ', suma
            resA = []
            resA = A[suma:]

            if len(resA)<4:
                res = resA
            else:
                res = resA[:4]
            resultado.append(res)
            break
        else:
            resA = []
            resA= A[suma:suma+12]
            res = resA[:4]
            suma = suma + 12
            resultado.append(res)

    return resultado

def dividir(B, num):
    result = []
    suma = 0
    aux = []
    for x in B:
        for y in range(0, len(x)):
            aux.append(x[y])

    print 'aux', aux
    for i in range(0, len(aux)):
        if suma >= len(aux):
            break
        elif suma + num >= len(aux):
            resA = []
            resA = aux[suma:]


            result.append(resA)
            break
        else:
            resA = []
            resA = aux[suma:suma + num]
            suma = suma + num
            result.append(resA)


    return result


def getmensajeFuente(C):
    alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz:.,;��!()?"
    print len(alf)
    res = ''
    for x in C:
        aux = ''
        for y in x:
            aux = aux + str(y)
        a = int(aux, 2)
        res = res + alf[a]


    return res

#Ejercicio 1


modelo01_lista01=[0,1,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,0,0,1,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,0,1,0,1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0,1,1,0,1,0,0,1,1,0,1,1,0,1,1,0,1,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
A=[]

B = getMensajeLineal(modelo01_lista01)

print B

C = dividir(B,7)

print getmensajeFuente(C)


