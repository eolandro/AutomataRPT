###############################
# 1 = Piedra
R = 1
# 2 = Papel
P = 2
# 3 = Tijera
T = 3
# Vacio = Empate
E = 0
###############################


def cabezal(C):
	# T P R
	if C == R:
		return [E,P,R]
	if C == P:
		return [P,E,T]
	if C == T:
		return [R,T,E]
	if C == E:
		return [R,P,T]

def subconjunto(A,B):

	#Piedra
	if A == R and B == R:
		return E
	if A == R and B == P:
		return P
	if A == R and B == T:
		return R
	#Papel
	if A == P and B == R:
		return P
	if A == P and B == P:
		return E
	if A == P and B == T:
		return T
	#Tijera
	if A == T and B == R:
		return R
	if A == T and B == P:
		return T
	if A == T and B == T:
		return E
	#Si son 0 
	if A == E:
		return B
	if B == E:
		return A

def generardesde(Cinta):
	# Vacio = Empate
	if not Cinta:
		return False
	Buffer = []
	despl = 0
	for j in Cinta:
		Resp = (despl*[E]) +  cabezal(j)
		despl = despl + 1
		Buffer.append(Resp)
		if (len(Buffer) == 2):
			PP = Buffer.pop()
			QQ = Buffer.pop() + [E]
			#print(QQ)
			#print(PP)
			RR = [ subconjunto(PP[i],QQ[i]) for i in range(len(QQ)) ]
			Buffer.append(RR)
			#print('#',RR)
	RR = Buffer.pop()
	return RR


def automata(Cinit,N):
	RR = Cinit
	i = 0
	while i < N:
		RR = generardesde(RR)
		yield RR
		i = i + 1


