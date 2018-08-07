"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

    All numbers will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

def combinationSum3(k,n):
	res=[]
	def dfs(k,remainder,res,temp,start):
		if k==0 and remainder==0:
			res.append(temp[:])
			return
		for i in range(start,10):
			if i>remainder:
				break
			temp.append(i)
			dfs(k-1,remainder-i,res,temp,i+1)
			temp.pop()
		return res
	dfs(k,n,res,[],1)
	return res







