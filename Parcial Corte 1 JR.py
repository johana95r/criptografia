import random

PC_1 =        [57, 49, 41, 33, 25, 17,  9]
PC_1 = PC_1 + [ 1, 58, 50, 42, 34, 26, 18]
PC_1 = PC_1 + [10,  2, 59, 51, 43, 35, 27]
PC_1 = PC_1 + [19, 11,  3, 60, 52, 44, 36]
PC_1 = PC_1 + [63, 55, 47, 39, 31, 23, 15]
PC_1 = PC_1 + [ 7, 62, 54, 46, 38, 30, 22]
PC_1 = PC_1 + [14,  6, 61, 53, 45, 37, 29]
PC_1 = PC_1 + [21, 13,  5, 28, 20, 12,  4]

PC_2 =        [14, 17, 11, 24,  1,  5]
PC_2 = PC_2 + [ 3, 28, 15,  6, 21, 10]
PC_2 = PC_2 + [23, 19, 12,  4, 26,  8]
PC_2 = PC_2 + [16,  7, 27, 20, 13,  2]
PC_2 = PC_2 + [41, 52, 31, 37, 47, 55]
PC_2 = PC_2 + [30, 40, 51, 45, 33, 48]
PC_2 = PC_2 + [44, 49, 39, 56, 34, 53]
PC_2 = PC_2 + [46, 42, 50, 36, 29, 32]

KEY_ROT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]



E =     [32,  1,  2,  3,  4,  5]
E = E + [ 4,  5,  6,  7,  8,  9]
E = E + [ 8,  9, 10, 11, 12, 13]
E = E + [12, 13, 14, 15, 16, 17]
E = E + [16, 17, 18, 19, 20, 21]
E = E + [20, 21, 22, 23, 24, 25]
E = E + [24, 25, 26, 27, 28, 29]
E = E + [28, 29, 30, 31, 32,  1]

S1    = [ [], [],  [],  [] ]
S1[0] = [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7]
S1[1] = [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8]
S1[2] = [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0]
S1[3] = [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]

S2    = [ [], [],  [],  [] ]
S2[0] = [15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10]
S2[1] = [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5]
S2[2] = [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15]
S2[3] = [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]

S3    = [ [], [],  [],  [] ]
S3[0] = [10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8]
S3[1] = [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1]
S3[2] = [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7]
S3[3] = [ 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]

S4    = [ [], [],  [],  [] ]
S4[0] = [ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15]
S4[1] = [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9]
S4[2] = [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4]
S4[3] = [ 3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]

S5    = [ [], [],  [],  [] ]
S5[0] = [ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9]
S5[1] = [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6]
S5[2] = [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14]
S5[3] = [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]

S6    = [ [], [],  [],  [] ]
S6[0] = [12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11]
S6[1] = [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8]
S6[2] = [ 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6]
S6[3] = [ 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]

S7    = [ [], [],  [],  [] ]
S7[0] = [ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1]
S7[1] = [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6]
S7[2] = [ 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2]
S7[3] = [ 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]

S8    = [ [], [],  [],  [] ]
S8[0] = [13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7]
S8[1] = [ 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2]
S8[2] = [ 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8]
S8[3] = [ 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]

P =     [12, 23, 8, 14]
P = P + [30, 9, 26, 4]
P = P + [24, 3, 17, 32]
P = P + [2, 13, 27, 16]
P = P + [19, 20, 1, 22]
P = P + [18, 7, 25, 28]
P = P + [6, 21, 15, 5]
P = P + [29, 10, 31, 11]


PI =      [58, 50, 42, 34, 26, 18, 10, 2]
PI = PI + [60, 52, 44, 36, 28, 20, 12, 4]
PI = PI + [62, 54, 46, 38, 30, 22, 14, 6]
PI = PI + [64, 56, 48, 40, 32, 24, 16, 8]
PI = PI + [57, 49, 41, 33, 25, 17,  9, 1]
PI = PI + [59, 51, 43, 35, 27, 19, 11, 3]
PI = PI + [61, 53, 45, 37, 29, 21, 13, 5]
PI = PI + [63, 55, 47, 39, 31, 23, 15, 7]

PF =      [40,  8, 48, 16, 56, 24, 64, 32]
PF = PF + [39,  7, 47, 15, 55, 23, 63, 31]
PF = PF + [38,  6, 46, 14, 54, 22, 62, 30]
PF = PF + [37,  5, 45, 13, 53, 21, 61, 29]
PF = PF + [36,  4, 44, 12, 52, 20, 60, 28]
PF = PF + [35,  3, 43, 11, 51, 19, 59, 27]
PF = PF + [34,  2, 42, 10, 50, 18, 58, 26]
PF = PF + [33,  1, 41,  9, 49, 17, 57, 25]

def genOcteto():
    res = ''
    par = 0
    for i in range(7):
        b = random.randint(0, 1)
        res = res + str(b)
        if b == 1:
            par = par + 1

    if par % 2 == 0:
        res = res + '1'
    else:
        res = res + '0'

    return res

def genKey():
    res = ''
    for i in range(8):
        res = res + genOcteto()
    return res

def permutar(dat, tab):
    res = ""
    for caso in tab:
        res = res + dat[caso-1]

    return res

def rotIzq(val, can):
    tmp = val[0:can]
    val = val+tmp
    return val[can:]

def subKeys(key):

    res = []

    pk = permutar(key, PC_1)
    lk = pk[0:28]
    rk = pk[28:]

    for rot in KEY_ROT:
        lk = rotIzq(lk, rot)
        rk = rotIzq(rk, rot)
        tk = permutar((lk+rk), PC_2)
        res.append(tk)

    return res

def xor(a, b):
    res = ''
    for i in range(len(a)):
        if(a[i] == b[i]):
            res = res+"0"
        else:
            res = res+"1"
    return res

def sacar(bits, caja):
    b = bits[0]+bits[5]
    c = bits[1:5]

    b = int(b, 2)
    c = int(c, 2)

    val = caja[b][c]
    val = bin(val)

    val = val.split('b')[1]
    dif = 4-len(val)
    val = (dif*"0")+val

    return val

def F(blo, key):

    bp = permutar(blo, E)
    bi = xor(bp, key)

    c1 = bi[0:6]
    c2 = bi[6:12]
    c3 = bi[12:18]
    c4 = bi[18:24]
    c5 = bi[24:30]
    c6 = bi[30:36]
    c7 = bi[36:42]
    c8 = bi[42:48]

    res = ""
    res = res + sacar(c1, S1)
    res = res + sacar(c2, S2)
    res = res + sacar(c3, S3)
    res = res + sacar(c4, S4)
    res = res + sacar(c5, S5)
    res = res + sacar(c6, S6)
    res = res + sacar(c7, S7)
    res = res + sacar(c8, S8)

    res = permutar(res, P)

    return res

def Des(blo, keys):

    bi = permutar(blo, PI)
    lb = bi[0:32]
    rb = bi[32:]

    for i in range(16):
        tb = F(rb, keys[i])
        lb = xor(lb, tb)

        cam = rb
        rb = lb
        lb = cam

    res = rb+lb
    res = permutar(res, PF)

    return res

def texto_binario(texto):
    texto = bytearray(texto, "UTF8")
    final = ""
    for x in texto:
        te = bin(x)
        te = te.split("b")[1]
        if(len(te) < 8):
            te = ("0" * (8-len(te)))+ te
        final=final+te
    return final

def bloque64(tex):
    var = []
    for i in range(0, len(tex), 64):
        bloqu = tex[i:i+64]
        if (len(bloqu) < 64):
            diferencia = (64 - len(bloqu))
            bloqu = ("0"*diferencia)+bloqu
        var.append(bloqu)
    return var

def bloqueDES(bloq, sks):
    text = ""
    for i in bloq:
        ecrp = Des(i, sks)
        text = text + ecrp

    return text


op = input("1. Generar clave 2. Cifrar 3. Decifrar Op?: ")

# 0111000001000110010011110110010001010001010000001001000111011010
## D:\Users\acer\Desktop\hola.txt

if(op == '1'):
    key = genKey()
    print (key)

if(op == '2'):
    cl = input("Ingrese clave: ")
    ar = input("Archivo: ")
    sks = subKeys(cl)
    f = open(ar, "r")
    datos = f.read()
    f.close()

    o = texto_binario(datos)
    bloq = bloque64(o)
    textoEncriptado = bloqueDES(bloq, sks)



    f = open(ar+".cif", "w")
    f.write(textoEncriptado)
    f.close()

elif(op == '3'):
    cl = input("Ingrese clave: ")
    ar = input("Archivo: ")
    sks = subKeys(cl)
    f = open(ar, "r")
    datos = f.read()
    f.close()
    sks.reverse()

    text = ""

    for i in range(0, len(datos), 64):
        bloque = datos[i:i+64]
        #print(len(bloque))
        bloque = Des(bloque, sks)

        text = text + bloque

    final = ""
    for i in range(len(text)):
        tex = text[i*8:((i+1)*8)]
        
        if(tex != "00000000" and tex != ""):
            ent = int(tex, 2)
            car = chr(ent)
            final = final + car


    f = open(ar+".des", "w")
    f.write(final)
    f.close()
