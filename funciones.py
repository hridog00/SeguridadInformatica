import math;
import operator;

def duplicar(f):
    res =[]

    for i in f:
        for x in f:

            res.append(i*x)


    return res

def asignarProbabilidades(f):
    total  = 0.0
    for elem in f:
        total = total + elem

    p = {}
    x = 0

    # asociar probabilidades a simbolos

    for elem in f:

        if x < 10:
            simbolo = 'a00' + str(x)
        else:
            if x < 100:
                simbolo = 'a0' + str(x)
            else:
                simbolo = 'a' + str(x)

        p[simbolo] = elem / total
        x = x + 1

    return p

def crearMatrizResultado(p):
    c = {}
    for elem in p:
        c[elem] = ''

    return c

def calcularEntropia(p):
    entropia = 0

    for x in p:
        entropia = entropia + (p[x] * math.log((1 / p[x]), 2))

    return entropia

def calcularHuffman(p,c):
    print 'FRECUENCIAS INICIALES'

    while len(p) > 1:

        # cogemos las menosres probabilidades

        aux = sorted(p.items(), key=operator.itemgetter(1), reverse=False)

        e1 = aux[0][0];
        e2 = aux[1][0];

        pos = 0
        while pos < len(e1):
            sim = e1[pos:pos + 4]

            c[sim] = c[sim] + '0'
            pos = pos + 4
        pos = 0
        while pos < len(e2):
            sim = e2[pos:pos + 4]
            c[sim] = c[sim] + '1'
            pos = pos + 4

        p[e1 + e2] = p[e1] + p[e2];
        p.pop(e1);
        p.pop(e2);

    return c

def obtenerLongitud(c, inicial):
    long = 0;
    for elem in inicial:
        long = long + inicial[elem] * len(c[elem])

    return long

def obtenerEficacia(entropia, long):
    eficacia = entropia / (math.log(2, 2) * long)
    return eficacia


#ejercicio 1
f = [83, 69, 67, 82, 69, 84, 79, 32, 68, 69, 32, 85, 78, 79, 32, 83, 69, 67, 82, 69, 84, 79, 32, 83, 69, 71, 85, 82, 79]
total = 0.0



f= duplicar(f)

p = asignarProbabilidades(f)

inicial = p.copy();
c = crearMatrizResultado(p)

entropia = calcularEntropia(p)

print entropia
c = calcularHuffman(p,c)
longitud = obtenerLongitud(c,inicial)
print longitud
eficacia = obtenerEficacia(entropia,longitud)
print eficacia


