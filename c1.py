import base64 as b64

DIC = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=*"

# Cifrar
def rotIzq(ele, can):
	global DIC
	pos = DIC.find(ele)
	pos = pos - can
	
	if(pos < len(DIC) and pos >= 0):
		return DIC[pos]
	else:
		return DIC[len(DIC)+pos]

# Decifrar
def rotDer(ele, can):
	global DIC
	pos = DIC.find(ele)
	pos = pos + can
	
	if(pos < len(DIC)):
		return DIC[pos]
	else:
		return DIC[pos-len(DIC)]

op = input("1. Cifrar - 2. Decifrar Op?: ")
texto = input("Texto?: ")
clave = input("Clave?: ")

if(op == '1'):
	texto = b64.b64encode(texto.encode('utf8')).decode('utf8')
	falta = len(texto) % 10
	texto = texto+("*"*(10-falta))
	
	for z in range(3):
		factor = len(texto) / 10
		
		mat = []
		tem = []
		
		for i in range(len(texto)):
			tem.append(texto[i])
			if(len(tem) == 10):
				mat.append(tem)
				tem = []
		
		tras = []
		tem = []
		for i in range(len(mat[0])):
			for j in range(len(mat)):
				tem.append(mat[j][i])
				if(len(tem) == factor):
					tras.append(tem)
					tem = []
		
		cif = ''
		for r in tras:
			cif = cif+''.join(r)
		
		cif2 = ''
		cclave = 0
		for i in range(len(cif)):
			des = int(clave[cclave])
			cif2 = cif2 + rotIzq(cif[i], des)
			
			cclave = cclave+1
			if(cclave == len(clave)):
				cclave = 0
		
		texto = cif2
	
	print(texto)

else:
	factor = len(texto) / 10
	
	for i in range(3):
		clear1 = ''
		cclave = 0
		for i in range(len(texto)):
			des = int(clave[cclave])
			clear1 = clear1 + rotDer(texto[i], des)
			
			cclave = cclave+1
			if(cclave == len(clave)):
				cclave = 0
		
		mat = []
		tem = []
		
		for i in range(len(clear1)):
			tem.append(clear1[i])
			if(len(tem) == factor):
				mat.append(tem)
				tem = []
		
		tras = []
		tem = []
		for i in range(len(mat[0])):
			for j in range(len(mat)):
				tem.append(mat[j][i])
				if(len(tem) == 10):
					tras.append(tem)
					tem = []
		
		clear2 = ''
		for r in tras:
			clear2 = clear2+''.join(r)
		texto = clear2
	
	texto = b64.b64decode(texto.encode('utf8')).decode('utf8')
	print(texto)
