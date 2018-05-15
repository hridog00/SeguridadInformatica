# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
import sys
print sys.stdout.encoding

def obtenerMensaje(m, c):
    alf = 'aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ0123456789 ,.:-()'
    Z = len(alf)
    mNum = []
    cNum = []
    dNum = []
    clave = []
    mensajeNum = []
    mensaje = ""
    clave_descifrado = ""
    for i in m:
        mNum.append(alf.find(i))
    for i in c:
        cNum.append(alf.find(i))

    for i in cNum:
        dNum.append(-i)

    print len(dNum)
    cola = len(mNum)%len(dNum)
    div = 0
    div = len(mNum)/len(dNum)
    for i in range (0, div):
        for j in dNum:
            clave.append(j)
    for i in range(0, cola):
        clave.append(dNum[i])

   # print 'Clave descifrado numerico ',dNum
    for i in dNum:
        clave_descifrado = clave_descifrado +alf[i]
    print "Clave descifrado ", clave_descifrado

    for i in range (0, len(mNum)):
        mensajeNum.append((mNum[i] + clave[i])%Z)

    for i in mensajeNum:
        mensaje = mensaje +alf[i]

    return mensaje


mensaje_cifrado=["3O0ONvTNSVCtZZVPCNyNPNXXG0t7TGEA2T4EEDy,vE1YNDAVT5vAUQV",
"AKsFGKUVy4NAtnvXGFB,yWVFM5zy,yN5zyR2A9wJ4FBRtT5yAKwF4YE9",
"LG3ROE1LwEWKPEMZRtMVwLJKFAU3DtJTHI25VADKGEC2DtQZSOL8LTJ",
"wc)Xdlyl02pu24.abu4kAtRf CFc0,pq48saXeTnpg8bnaXoahyg47ikFs",
"pvW b Y6hulWrYQ-qf hUa(10eb mFnaX)iblbyl26Yjb Fyp(,eena",
"Ct3SGVINR2QuCV7KZJyZCSCYROIMFGRO0yVPVRXVDLNAG(OCXRvSRy-QRSF",
"OUpFOFtRaQNyASBJYFuKwJ4Tt9hGVFtWpSTNRKtZ,yBZlSGIE2hS6JtUl",
"HLURytk,SOWXRtZ,HtMVVDNKPU7KQIW4RtJ2JURVQtUVwIWTXLL5wEUKGI1ZPUU5",
"jq3b BSaTfleVfikFdV2LtRXdBQc42F.9haCJ 4fau,XpyJs4fjkRY Fyc-fveZ4",
"mB3 Z52j,esys63,egijFd.Q1a,lhX :X9:crhX 51(aocpF,R06jfrvz a52nsazA"]


claves_cifrado=["CAJFN","ARhFNF","DAJR","hcR4ahFa09","ahFaYXY:b",
    "CAJFN","ARhFNF","DAJR","hcR4ahFa09","ahFaYXY:b"]



mensaje_cifrado2=["ZKXLxpZFKÉFvOPÑOAAABLKYvVp5PryFÚMÑIFsp5vBOZCzvRPPpFNÍÉ",
"JpZfvÓPRx1JrISP3pÑhV2ÑWfÑYOIEvWK8aF9v8vF2wÓfÑYOIfv0v7zF3",
"RITvQRy:IÑOtIJQñpINFtHFIibZVBtvIRñú33BupÍRanÑEÍHMÚPxj9J",
"daÉvd0Z(aaJs96W SVeákéayvvV91cñPn0jÚsjvv5,éosvs:ídrjOd5 1s",
"puT á8U5hujTrUÑ-pé fRa(XWéá lBnaT)iálávlY4Uíá Evp(,eena",
"xp0OrÓÑFJMUwrN0JWwAÑyOAÚBIÑÉxpVPÓpÑOTEYJzHJxr,UvPÁAUFp9PÓFF",
"YzVfDJpÑaNJpÑhVÑHÑáv0A7uv3vÓoBEBVsIRÑIrV pÓñFWpQjNJÍ9jvNA",
"ÑNKvBIYv5YOFKA6AfINFRzJIrv(EOHJUIfnU5JDÍAZj.VWETHI4afZEÉHOÑ0An3",
"4orP ce1 sFc0j,dfÉ.PúéaaÉu996 Evsc6íeaFnPjh vTeá,acñB,PóÚcuOoYa1",
"mA0 V2Yí,eqvs309egiiBd,ÑXa,lfU :T7.crfU 2X(añcñB,OW3íéruw a2Yñsayx"]

claves_cifrado2=["xvFB","JvÑfB","JBzvFÑfbÑ","1afBaV6","afBaUTU.á",
    "xvFB","JvÑfB","JBzvFÑfbÑ","1afBaV6","afBaUTU.á"]

for i in range(0, len(mensaje_cifrado)):
    print obtenerMensaje(mensaje_cifrado2[i],claves_cifrado2[i])