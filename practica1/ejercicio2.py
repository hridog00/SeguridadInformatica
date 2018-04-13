import math;
import operator;

def duplicar(f):
    res =[]
    print f

    for i in f:
        for x in f:
            for j in f:
                for y in f:

                    res.append(i*x*j*y)


    return res

def arbolGrand(f):
    total = 0.0
    tam = 0
    for elem in f:
        total = total + elem
        tam = tam +1

    print tam
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

    while len(p) > 1:

        # cogemos las menosres probabilidades

        aux = sorted(p.items(), key=operator.itemgetter(1), reverse=False)
        print 'ENTRO'
        e1 = aux[0][0];
        e2 = aux[1][0];
        print e1
        print e2
        pos = 0
        while pos < len(e1):

            sim = e1[pos:pos + 5]
            print 'Sim', sim
            c[sim] = c[sim] + '0'
            pos = pos + 5
        pos = 0
        while pos < len(e2):
            sim = e2[pos:pos + 5]
            c[sim] = c[sim] + '1'
            pos = pos + 5

        p[e1 + e2] = p[e1] + p[e2];
        print e1+e2
        p.pop(e1);
        p.pop(e2);

    long = 0;
    for elem in inicial:
        long = long + inicial[elem] * len(c[elem])

    eficacia = entropia / (math.log(2, 2) * long)


    return eficacia
fi = [32, 45, 27, 33]

f4 = duplicar(fi);
eficacia4 = arbolGrand(f4)
print 'Eficacia ', eficacia4