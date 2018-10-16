"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  

    1 is typically treated as an ugly number.
    n does not exceed 1690.

"""

def nthUglyNumber(n):
	if n==0:
		return False

	k=[0 for _ in range(n)]
	k[0]=1
	# pointer for tracking the min 
	t2,t3,t5=0,0,0

	for i in range(1,n):
		k[i]=min(k[t2]*2,min(k[t3]*3,k[t5]*5))
		if k[i]==k[t2]*2:
			t2+=1
		if k[i]==k[t3]*3:
			t3+=1
		if k[i]==k[t5]*5:
			t5+=1
	return k[n-1]

	




