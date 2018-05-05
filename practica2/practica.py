import numpy as np

def generarPalabrasQarias(q, k, res, re):
    a = len(re)
    if a < k:
        for i in range(0, q):
            aux = []

            aux = re[:]
            aux.append(i)

            generarPalabrasQarias(q, k, res, aux)

    else:
        res.append(re)
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

def buscarPesos(G, P,q):
   # v = np.multiply(P, G)
    v = np.dot(P,G)
    res = v%q
    #for x in range(0,len(res)):
     #   print res[x]

    min = 100000000000
    for i in range(0, len(res)):
        aux = 0
        for j in range(0, len(res[i])):

            if res[i][j] != 0:
                aux = aux + 1

        if aux < min:
            if aux != 0:
                min = aux

    print min
    return min

re = []
res = []
#A = [[0,2,1,1],[1,1,2,1],[1,1,1,2]]
#A=[[1,1,0],[1,0,1]]
A=[[1,1,0,1,1,1,0,0,0,1,0,1],
[1,0,1,1,1,0,0,0,1,0,1,1],
[0,1,1,1,0,0,0,1,0,1,1,1],
[1,1,1,0,0,0,1,0,1,1,0,1],
[1,1,0,0,0,1,0,1,1,0,1,1],
[1,0,0,0,1,0,1,1,0,1,1,1],
[0,0,0,1,0,1,1,0,1,1,1,1],
[0,0,1,0,1,1,0,1,1,1,0,1],
[0,1,0,1,1,0,1,1,1,0,0,1],
[1,0,1,1,0,1,1,1,0,0,0,1],
[0,1,1,0,1,1,1,0,0,0,1,1],
[1,1,1,1,1,1,1,1,1,1,1,0]]
q = 2
matrizG = getMatrizGeneradora(A)
generarPalabrasQarias(q,len(A), res, re)

distanciaMin = buscarPesos(matrizG, res, q)


