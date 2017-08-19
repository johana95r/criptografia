def rotIzq(val, mov):
    val = val-mov
    
    if(val >= 0):
        return val
    else:
        return 256+val

def rotDer(val, mov):
    val = val+mov
    
    if(val <= 255):
        return val
    else:
        return val-256

op = input("1. Cifrar 2. Decifrar Op?: ")
ar = input("Archivo?: ")
cl = input("Clave: ")

if(op == '1'):
    f = open(ar, "rb")
    datos = f.read()
    f.close()
    
    sal = bytearray()
    cc = 0
    for b in datos:
        sal.append(rotDer(b, int(cl[cc])))
        cc = cc+1
        if(cc == len(cl)):
            cc = 0
    
    print(sal)
    f = open(ar+".cif", "wb")
    f.write(sal)
    f.close()
    
elif(op == '2'):
    f = open(ar, "rb")
    datos = f.read()
    f.close()
    
    sal = bytearray()
    cc = 0
    for b in datos:
        sal.append(rotIzq(b, int(cl[cc])))
        cc = cc+1
        if(cc == len(cl)):
            cc = 0
    
    f = open(ar+".des", "wb")
    f.write(sal)
    f.close()
    
    
