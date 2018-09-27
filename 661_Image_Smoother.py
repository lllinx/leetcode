"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:

Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
"""

def imageSmoother(M):
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


	