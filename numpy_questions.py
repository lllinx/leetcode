import numpy as np
def linear_congruence(seed, A, B, M, n):
	x=seed
	for i in range(n):
		x=np.mod(A*x+B,M)
		print(x)


def linear(seed, A, B, M):
	x=seed
	length=[]
	for m in M:
		output=[x,]
		Non_repeat=True
		while Non_repeat==True:
			x=np.mod(A*x+B,m)
			if x in output:
				Non_repeat=False
			else:
				output.append(x)
		length.append(len(output))
	return length

a=range(11,200)
b=linear(137,3,7,a)
import matplotlib.pyplot as plt
plt.plot(a,b,'ro')
plt.show()
		






		

