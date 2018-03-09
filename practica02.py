import operator
p = {'a':0.3,'b': 0.2, 'c':0.1, 'd':0.1, 'e':0.05, 'f':0.05, 'g':0.05, 'h':0.05, 'i':0.05, 'j':0.05}
c={'a':'','b': '', 'c':'', 'd':'', 'e':'', 'f':'', 'g':'', 'h':'', 'i':'', 'j':''}

#p={'a': 0.3, 'b': 0.2, 'c': 0.2, 'd': 0.1, 'e': 0.1, 'f':0.1}
#c={'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f':''}

f=[27,16,4,56,22,2,78,45,36,13,12,7]

total = 0.0
for elem in f:
    total = total + elem
p={}
c={}
print total
letras = 'abcdefghijklmnopqrstuvwxyz'
variable = 0
for elem in f:

    p[letras[variable]] = elem/total;
    c[letras[variable]] = ''
    variable = variable +1


texto = "La noche cae, brumosa ya y morada. Vagas claridades malvas y verdes perduran tras la torre de la iglesia. El camino sube, lleno de sombras, de campanillas, de fragancia de hierba, de canciones, de cansancio y de anhelo."
#texto = 'secreto de uno secreto seguro'
print 'primer valor ',texto[0]
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


inicial = p.copy();
print 'FRECUENCIAS INICIALES'
print p

while len(p)>1:

    #cogemos las menosres probabilidades

    aux = sorted(p.items(), key=operator.itemgetter(1), reverse=False)
    print aux
    e1 = aux[0][0];
    e2 = aux[1][0];
    print 'Elemento 1: ', e1
    print 'Elemento 2: ', e2

    for letra in e1:
        c[letra] = '0'+c[letra];
    for letra in e2:
        c[letra] = '1'+c[letra] ;
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



