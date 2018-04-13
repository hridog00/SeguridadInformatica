import math;
import operator;

def duplicar(f):
    res =[]

    for i in f:
        for x in f:

            res.append(i*x)


    return res
def duplicar3():
    res = []
    for i in f:
        for x in f:
            for j in f:
                res.append(i*x*j)



#ejercicio 1
f = [83, 69, 67, 82, 69, 84, 79, 32, 68, 69, 32, 85, 78, 79, 32, 83, 69, 67, 82, 69, 84, 79, 32, 83, 69, 71, 85, 82, 79]
total = 0.0



f= duplicar(f)
for elem in f:
    total = total + elem
p={}
c={}
print total
letras = 'abcdefghijklmnopqrstuvwxyzABC'
simbolo = ''
x = 0

#asociar probabilidades a simbolos

for elem in f:
    if x < 10:
        simbolo = 'a00' + str(x)
    else:
        if x < 100:
            simbolo = 'a0' + str(x)
        else:
            simbolo = 'a' + str(x)

    p[simbolo] = elem/total;
    c[simbolo] = ''
    x = x +1

#hallar entropia
entropia = 0

for x in p:
    entropia= entropia + (p[x] * math.log((1/p[x]),2))

print 'ENTROPIA'
print entropia

#huffman

inicial = p.copy()
print 'FRECUENCIAS INICIALES'
print p

while len(p)>1:

    #cogemos las menosres probabilidades

    aux = sorted(p.items(), key=operator.itemgetter(1), reverse=False)

    e1 = aux[0][0];
    e2 = aux[1][0];

    pos = 0
    while pos < len(e1):
        sim = e1[pos:pos+4]

        c[sim] = c[sim] + '0'
        pos = pos +4
    pos = 0
    while pos <len(e2):
        sim = e2[pos:pos + 4]
        c[sim] = c[sim] + '1'
        pos = pos + 4




    p[e1 + e2] = p[e1]+p[e2];
    p.pop(e1);
    p.pop(e2);

print 'RESULTADO FINAL'
print(c)

print 'LONGITUD MEDIA'
long = 0;
for elem in inicial:
    long = long + inicial[elem] * len(c[elem])

print long

print 'EFICACIA'

eficacia = entropia/(math.log(2,2)*long)
print eficacia




