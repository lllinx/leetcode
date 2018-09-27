"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""

def findKthLargest(nums, k):
	result=[[0 for i in range(len(M[0]))] for j in range(len(M))]
	for i in range(len(M)):
		for j in range(len(M[0])):
			count=0
			ans=0
			for r in (i-1,i,i+1):
				for c in (j-1,j,j+1):
					if 0<=r<len(M) and 0<=c<len(M[0]):
						ans+=M[r][c]
						count+=1
			result[i][j]=int(ans/count)
	return result

