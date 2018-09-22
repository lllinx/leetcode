"""
48. Rotate Image
ou are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""

def rotate(matrix):
	"""
	:type matrix: List[List[int]]
	:rtype: void Do not return anything, modify matrix in-place instead.
	"""
	# divide to 2 step of transpose and flip
	for i in range(len(matrix)):
		for j in range(i+1,len(matrix)):
			matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
	for row in matrix:
		row[:]=row[::-1]
	return matrix




        