"""7. Reverse Integer"""
def reverse(x):
		"""
		:type x: int
		:rtype: int
		"""
		s=[]
		if x>=0:
			while x!=0:
				s.append(x%10)
				x=x//10
			new_x=sum([s[i]*pow(10,len(s)-i-1) for i in range(len(s))])
			return new_x
		else:
			return -1*reverse(-x)
reverse(123)
reverse(-123)
reverse(120)
