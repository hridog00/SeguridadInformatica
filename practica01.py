import operator

texto =  'Existe una cosa muy misteriosa, pero muy cotidiana. Todo el mundo participa de ella, todo el mundo la conoce, pero muy pocos se paran a pensar en ella. Casi todos se limitan a tomarla como viene, sin hacer preguntas. Esta cosa es el tiempo.'

#texto = 'secreto de uno secreto seguro'
print 'primer valor ',texto[0]
dict = {texto[0] : 0.0}
dictAux = {texto[0] : 0.0}

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
    dictAux[x] = dict[x]/total
    prob = prob + dictAux[x]
    print x ,':',dict[x] ,':',dictAux[x]



aux = sorted(dictAux.items(), key=operator.itemgetter(1), reverse=True)
print(aux);
resultado = {}
print 'RESULTADO'
for x in range(0, 5):

    resultado[aux[x][0]] = [dict[aux[x][0]],aux[x][1]]
    print aux[x][0], ':',  resultado[aux[x][0]]

print resultado


