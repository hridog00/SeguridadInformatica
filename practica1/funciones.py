import math;
import operator;

def duplicar(f):
    res =[]

    for i in f:
        for x in f:

            res.append(i*x)


    return res
def duplicar3(f):
    res = []
    for i in f:
        for x in f:
            for j in f:
                res.append(i*x*j)

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

def arbolGrand(f):
    total = 0.0
    for elem in f:
        total = total + elem

    p = {}
    c ={}
    x = 0

    # asociar probabilidades a simbolos

    for elem in f:

        if x < 10:
            simbolo = 'a000' + str(x)
        else:
            if x < 100:
                simbolo = 'a00' + str(x)
            else:
                if x < 1000:
                    simbolo = 'a0' + str(x)
                else:
                    simbolo = 'a' + str(x)



        p[simbolo] = elem / total
        c[simbolo] = ''
        x = x + 1

    entropia = 0
    inicial = p.copy()
    for x in p:
        entropia = entropia + (p[x] * math.log((1 / p[x]), 2))

    print c
    while len(p) > 1:

        # cogemos las menosres probabilidades

        aux = sorted(p.items(), key=operator.itemgetter(1), reverse=False)

        e1 = aux[0][0];
        e2 = aux[1][0];

        pos = 0
        while pos < len(e1):
            sim = e1[pos:pos + 5]

            c[sim] = c[sim] + '0'
            pos = pos + 5
        pos = 0
        while pos < len(e2):
            sim = e2[pos:pos + 5]
            c[sim] = c[sim] + '1'
            pos = pos + 5

        p[e1 + e2] = p[e1] + p[e2];
        p.pop(e1);
        p.pop(e2);

    long = 0;
    for elem in inicial:
        long = long + inicial[elem] * len(c[elem])

    eficacia = entropia / (math.log(2, 2) * long)

    return eficacia


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

def calcularHuffmanText(p,c):
    while len(p) > 1:

        # cogemos las menosres probabilidades

        aux = sorted(p.items(), key=operator.itemgetter(1), reverse=False)
        print aux
        e1 = aux[0][0];
        e2 = aux[1][0];
        print 'Elemento 1: ', e1
        print 'Elemento 2: ', e2

        for letra in e1:
            c[letra] = '0' + c[letra];
        for letra in e2:
            c[letra] = '1' + c[letra];
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

def obtenerLongCodificado (texto, c):
    longitud = 0.0;
    for x in texto:

        longitud = longitud + len(c[x])
    return longitud

#ejercicio 1
texto = "Me viene ahora el recuerdo de las noches en la calle de Aribau. Aquellas noches que corrian como un rio negro, bajo los puentes de los dias, y en las que los olores estancados despedian un vaho de fantasmas."

dict = {texto[0] : 0.0}
p = {texto[0] : 0.0}

c={}
total = 0.0
for x in texto:
    total = total + 1.0
    if dict.has_key(x):
        dict[x] = dict[x] +1.0
    else:
        dict[x] = 1

print total
prob = 0.0
for x in dict:
    p[x] = dict[x]/total
    c[x] = ''
    prob = prob + p[x]
    print x ,':',dict[x] ,':',p[x]

print p

inicial = p.copy();

c = calcularHuffmanText(p,c)

longitud = obtenerLongitud(c,inicial)
print longitud
longitudT = obtenerLongCodificado(texto,c)
print 'Longitud ',longitudT

#ejercicio 2

fi = [32, 45, 27, 33]
pi =asignarProbabilidades(fi)
ini = pi.copy()
ci = crearMatrizResultado(pi)
ent1 = calcularEntropia(pi)
ci = calcularHuffman(pi, ci)
long1 = obtenerLongitud(ci, ini)
eficacia1 = obtenerEficacia(ent1, long1)
print eficacia1
f2 =duplicar(fi)
p2 =asignarProbabilidades(f2)
ini2 = p2.copy()
print p2
c2 = crearMatrizResultado(p2)
ent2 = calcularEntropia(p2)
c2 = calcularHuffman(p2, c2)
long2 = obtenerLongitud(c2, ini2)
eficacia2 = obtenerEficacia(ent2, long2)
print eficacia2

f3 = duplicar3(fi)
p3 =asignarProbabilidades(f3)
ini3 = p3.copy()
print p3
c3 = crearMatrizResultado(p3)
ent3 = calcularEntropia(p3)
c3 = calcularHuffman(p3, c3)
long3 = obtenerLongitud(c3, ini3)
eficacia3 = obtenerEficacia(ent3, long3)
print eficacia3

f4 = duplicar(f3);
#eficacia4 = arbolGrand(f4)
print 'Eficacia'
#print eficacia4


#ejercicio3
prob  = {'a000':0.0}
prob['a000'] = 23/316.0
prob['a001'] = 47/316.0
prob['a002'] = 13/158.0
prob['a003'] = 9/158.0
prob['a004'] = 19/316.0
prob['a005'] = 11/158.0
prob['a006'] = 18/79.0
prob['a007'] = 11/316.0
prob['a008'] = 13/158.0
prob['a009'] = 19/316.0
prob['a010'] = 33/316.0
total = 0.0
for x in prob:
    print prob[x]
    total = total + prob[x]

print total



res = crearMatrizResultado(prob)
res = calcularHuffman(prob, res)

print res

longitudes = [4,4, 4,4, 4, 4, 2, 4, 4, 4, 3 ]
probb = [23, 47, 26, 18, 19, 22, 72, 11, 26, 19, 33]
total = 0
for x in longitudes:
    total = total + (longitudes[x]*probb[x])

total = total/316
print total















