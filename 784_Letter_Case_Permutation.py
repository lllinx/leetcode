"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Note:

    S will be a string with length at most 12.
    S will consist only of letters or digits.
"""

def letterCasePermutation(s):
	res=[""]
	for ch in s:
		if ch.isalpha():
			res=[i+j for i in res for j in [ch.upper(),ch.lower()]]
		else:
			res=[i+ch for i in res]
	return res

def letterCasePermutation2(s):
	res=[]
	def helper(s,res,index):
		if index==len(s):
			res.append(s)
			return
		if s[index].isalpha():
			s=s[:index]+s[index].lower()+s[index+1:]
			helper(s,res,index+1)
			s=s[:index]+s[index].upper()+s[index+1:]
			helper(s,res,index+1)
		else:
			helper(s,res,index+1)
		return res
	helper(s,res,0)
	return res
	





