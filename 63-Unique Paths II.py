"""
dynamic programming
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

def uniquepathwithobstacles(pathgrid):
	if pathgrid[0][0]==1:
		return 0
	for i in range(len(pathgrid)):
		for j in range(len(pathgrid[0])):
			if i==0 and j==0:
				pathgrid[i][j]=1
			elif pathgrid[i][j]==1:
				pathgrid[i][j]=0
			elif i==0:
				pathgrid[i][j]=pathgrid[i][j-1]
			elif j==0:
				pathgrid[i][j]=pathgrid[i-1][j]
			else:
				pathgrid[i][j]=pathgrid[i-1][j]+pathgrid[i][j-1]
	return pathgrid[-1][-1]





