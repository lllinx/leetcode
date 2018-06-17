"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

def getrow(rowindex):
	current=[1 for _ in range(rowindex+1)]
	if rowindex<2:
		return current

	i=2
	last=[1,1]
	while i<=rowindex:
		current=[1 for _ in range(i+1)]
		for j in range(1,i):
			current[j]=last[j-1]+last[j]
		last=current
		i+=1	
	return current

