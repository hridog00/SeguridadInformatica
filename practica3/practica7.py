# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
import sys
print sys.stdout.encoding

def obtenerMensaje(m, c):
    alf = 'a�bcde�fghi�jklmn�o�pqrstu�vwxyzA�BCDE�FGHI�JKLMN�O�PQRSTU�VWXYZ0123456789 ,.:-()'
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



mensaje_cifrado2=["ZKXLxpZFK�FvOP�OAAABLKYvVp5PryF�M�IFsp5vBOZCzvRPPpFN��",
"JpZfv�PRx1JrISP3p�hV2�Wf�YOIEvWK8aF9v8vF2w�f�YOIfv0v7zF3",
"RITvQRy:I�OtIJQ�pINFtHFIibZVBtvIR��33Bup�Ran�E�HM�Pxj9J",
"da�vd0Z(aaJs96W SVe�k�ayvvV91c�Pn0j�sjvv5,�osvs:�drjOd5 1s",
"puT �8U5hujTrU�-p� fRa(XW�� lBnaT)i�l�vlY4U�� Evp(,eena",
"xp0Or��FJMUwrN0JWwA�yOA�BI��xpVP�p�OTEYJzHJxr,UvP�AUFp9P�FF",
"YzVfDJp�aNJp�hV�H��v0A7uv3v�oBEBVsIR�IrV p��FWpQjNJ�9jvNA",
"�NKvBIYv5YOFKA6AfINFRzJIrv(EOHJUIfnU5JD�AZj.VWETHI4afZE�HO�0An3",
"4orP ce1 sFc0j,df�.P��aa�u996 Evsc6�eaFnPjh vTe�,ac�B,P��cuOoYa1",
"mA0 V2Y�,eqvs309egiiBd,�Xa,lfU :T7.crfU 2X(a�c�B,OW3��ruw a2Y�sayx"]

claves_cifrado2=["xvFB","Jv�fB","JBzvF�fb�","1afBaV6","afBaUTU.�",
    "xvFB","Jv�fB","JBzvF�fb�","1afBaV6","afBaUTU.�"]

for i in range(0, len(mensaje_cifrado)):
    print obtenerMensaje(mensaje_cifrado2[i],claves_cifrado2[i])