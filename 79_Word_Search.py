"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""

def exist(board,word):
	def backtrack(board,word,index,i,j):
		if index==len(word):
			return True
		if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
			return False
		if board[i][j]==word[index]:
			tmp=board[i][j]
			board[i][j]="#"
			res=backtrack(board,word,index+1,i+1,j) or backtrack(board,word,index+1,i-1,j) or backtrack(board,word,index+1,i,j+1) or backtrack(board,word,index+1,i,j-1)
			board[i][j]=tmp
			return res
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j]==word[0]:
				if backtrack(board,word,0,i,j):
					return True
	return False





