
# -*- coding: cp1252 -*-
def getMensajeLineal(A):
    resultado = []
    suma = 0
    for i in range(0,len(A)):
        print len(A), ' ', suma
        if suma>=len(A):

            break
        elif suma+7>=len(A):
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
            resA= A[suma:suma+7]
            res = resA[:4]
            suma = suma + 7
            resultado.append(res)

    return resultado

def dividir(B, lon):
    result = []
    suma = 0
    aux = []
    for x in B:
        for y in range(0, len(x)):
            aux.append(x[y])


    for i in range(0, len(aux)):
        if suma >= len(aux):
            break
        else:
            print
            res = []
            res = aux[suma:suma + lon]
            suma = suma + lon
            result.append(res)

    return result

def getmensajeFuente(C):
    alf = "abcde ABCDEfghijklmnFGHIJKLMNopqrstuvwxyzOPQRSTUVWXYZ.,;¿?¡!"
    res = ''
    for x in C:
        aux = ''
        for y in x:
            aux = aux + str(y)
        a = int(aux, 2)
        res = res + alf[a]


    return res





#A = [0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,1,0,1,0,1,1,1,1,0,1,0,0, 1,1]
A=[0,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1,0,0,1,
0,0,0,0,1,0,1,1,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,
1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,
0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,
0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,
1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,
0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,1,0,0,1,1,
0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,
1,0,0,0,1,0,1,1,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,
1,0,0,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,
0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,1,
0,0,0,0,1,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,1,
1,0,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,
0,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,
0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,1,
1,1,0,0,1,1,0,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,1,1,1,
1,1,0,1,1,0,0,1]

B= getMensajeLineal(A)
print 'B'
print B
C = dividir(B,6)
print getmensajeFuente(C)
