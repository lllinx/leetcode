"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true

Example 2:

Input: [6,5,4,4]
Output: true

Example 3:

Input: [1,3,2]
Output: false

Example 4:

Input: [1,2,4,5]
Output: true

Example 5:

Input: [1,1,1]
Output: true
"""

def isMonotonic(A):
	def increase(A):
		for i in range(len(A)-1):
			if A[i]>A[i+1]:
				return False
		return True
	def decrease(A):
		for i in range(len(A)-1):
			if A[i]<A[i+1]:
				return False
		return True
	return increase(A) or decrease(A)

def isMonotonic2(A):
	return all (A[i]>=A[i+1] for i in range(len(A)-1)) or all (A[i]<=A[i+1] for i in range(len(A)-1))

def isMonotonic3(A):
	increase,decrease=True,True
	for i in range(len(A)-1):
		if A[i]>A[i+1]:
			increase=False
		if A[i]<A[i+1]:
			decrease=False
	return increase or decrease

