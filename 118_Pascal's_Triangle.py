"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""

def generate(numRows):
	result=[[0 for i in range(j+1)] for j in range(numRows)]
	result[0][0]=1
	for i in range(1,numRows):
		for j in range(i+1):
			if j==0 or j==i:
				result[i][j]=1
			else:
				result[i][j]=result[i-1][j-1]+result[i-1][j]

	return result


