"""7. Reverse Integer"""
def reverse(x):
	"""
	:type x: int
	:rtype: int
	"""
	def inner(x):
		rev=0
		while x!=0:
			rev=rev*10+x%10
			x=x//10
			if rev<-2**31 or rev>2**31-1:
				return 0
		return rev
	if x>=0:
		return inner(x)
	return -inner(-x)

