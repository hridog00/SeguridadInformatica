len = ''

variable = 0
for x in range(0, 120):
    if x<10:
         len = 'a00' + str(x)
    else:
        if x < 100:
            len = 'a0' + str(x)
        else:
            len = 'a'+str(x)
    print len

print len[:2]

f4 = duplicar(f3)
p4 =asignarProbabilidades(f4)

ini4 = p4.copy()
c4 = crearMatrizResultado(p4)
print c4
ent4 = calcularEntropia(p4)
c4 = calcularHuffman(p4, c4)
long4 = obtenerLongitud(c4, ini4)
eficacia4 = obtenerEficacia(ent4, long4)
print eficacia4
