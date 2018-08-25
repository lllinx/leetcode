"""
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

def generateParenthesis(n):
	res=[]
	def backtrack(temp,res,left,right,size):
		if len(temp)==2*size:
			res.append(temp)
		if left<size:
			backtrack(temp+"(",res,left+1,right,size)
		if right<left:
			backtrack(temp+")",res,left,right+1,size)
		return res
	backtrack("",res,0,0,n)
	return res

