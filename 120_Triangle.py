"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

def minimumTotal(triangle):
	minlen=triangle[-1]
	for layer in range(len(triangle)-2,-1,-1):
		for i in range(layer+1):
			minlen[i]=min(minlen[i],minlen[i+1])+triangle[layer][i]
	return minlen[0]
