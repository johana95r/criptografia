import base64 as b64

DIC =  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=*"

op = input(" que quieres hacer: 1 encript, 2 desencript:? ")
texto = input("Ingrese el texto: ")
clave = input('Por favor digite clave: ')

def rotIzq(val, mov):
	global DIC
	pos = DIC.find(val)
	pos = pos + mov
	if (pos < len(DIC)):
		return  DIC[pos]
	else:
		return DIC[pos - len(DIC)]

def rotDer(val, mov):
	global DIC
	pos = DIC.find(val)
	pos = pos - mov
	if (pos < len(DIC) and pos >= 0):
		return  DIC[pos]
	else:
		return DIC[pos + len(DIC)]

### operacion matemtica
clave = int(clave)* int(clave)


#########

if (op == "1"):
	texto = b64.b64encode(texto.encode('utf8')).decode('utf8')

	 ## sustitucion 
	
	cif2 = ""
	cclave = 0
	clave = str(clave)
	for i in range(len(texto)):
		des = int(clave[cclave])
		cif2 = cif2 + rotDer(texto[i], des)
			
		cclave = cclave+1
		if(cclave == len(clave)):
			cclave = 0

	
	v1 = 0
	v2 = 1
	cclave = 0

	cif3 = ""

	cR = len(clave) / 2 
				
	for i in range (len(cif2)-int(cR)):
		des = int(clave[cclave])

		if(v1 <= len(cif2)-1):
			cifT1 = rotDer(cif2[v1], des)
			cifT2 = rotDer(cif2[v2], des)
			cclave = cclave+1
			cif3 = cif3 + cifT1 + cifT2
			v1 = v1+2
			v2 = v2+2
			cifT1 = ""
			cifT2 = ""
		if(cclave == len(clave)):
			cclave = 0

	print(cif3)

	### desencriptar
	
else: 
	v1 = 0
	v2 = 1
	cclave = 0 
	cif3 = ""
	clave=str(clave)
	cR = len(clave) / 2 			

	for i in range(len(texto)-int(cR)):

		des = int(clave[cclave])
		if(v1 <= len(texto)-1):

			cifT1 = rotIzq(texto[v1], des)
			cifT2 = rotIzq(texto[v2], des)
			cclave = cclave+1
			cif3 = cif3 + cifT1 + cifT2
			v1 = v1+2
			v2 = v2+2
			cifT1 = ""
			cifT2 = ""
			
		if(cclave == len(clave)):
			cclave = 0
	
	cif2 = ""
	cclave = 0
	for i in range(len(cif3)):
			des = int(clave[cclave])
			cif2 = cif2 + rotIzq(cif3[i], des)
			
			cclave = cclave+1
			if(cclave == len(clave)):
				cclave = 0
	
	cif2 = b64.b64decode(cif2.encode("utf8")).decode("utf8")
	print(cif2)