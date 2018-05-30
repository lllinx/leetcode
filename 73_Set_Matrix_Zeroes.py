"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

def setzeros(matrix):
  row=len(matrix)
  col=len(matrix[0])
  row_zero,col_zero=False,False

  for i in range(row):
    for j in range(col):
      if matrix[i][j]==0:
        matrix[i][0],matrix[0][j]=0,0
        if i==0:
          row_zero=True
        if j==0:
          col_zero=True

  for i in range(1,row):
    for j in range(1,col):
      if matrix[i][0]==0 or matrix[0][j]==0:
        matrix[i][j]=0

  if row_zero==True:
    for j in range(col):
      matrix[0][j]=0

  if col_zero==True:
    for i in range(row):
      matrix[i][0]=0

  return matrix
