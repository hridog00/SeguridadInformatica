import numpy as np

def errorPatron():

    return
def generarErrores(q, k, res, re):
    a = len(re)
    if a < k:
        for i in range(0, q):
            aux = []

            aux = re[:]
            aux.append(i)

            generarErrores(q, k, res, aux)

    else:
        res.append(re)




    return

def hallarPeso(error):
    min = 100000000000
    for j in range(0, len(error)):
        if error[j] != 0:
            error = error + 1
    if error < min:
        if error != 0:
            min = error
    return min

def tablero(errores, H):
    tablero = np.dot(H, errores)

    return
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

A=[[1,1,1],[1,1,0],[1,0,1],[0,1,1]]


print matrizControl(A)