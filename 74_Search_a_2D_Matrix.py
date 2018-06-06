"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
def searchmatrix(matrix,target):
	if matrix==[] or len(matrix[0])==0:
		return False
	m, n=len(matrix), len(matrix[0])
	low,high=0,m*n-1
	while low<=high:
		mid=(low+high)//2
		if target==matrix[mid//n][mid%n]:
			return True
		elif target>matrix[mid//n][mid%n]:
			low=mid+1
		else:
			high=mid-1
	return False




