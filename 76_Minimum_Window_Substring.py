"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

def minWindow(s,t):
	dic={}
	for t1 in t:
		if t1 not in dic:
			dic[t1]=1
		else:
			dic[t1]+=1

	begin, end=0, 0
	counter=len(dic)
	result=""

	while end<len(s):
		if s[end] in dic:
			dic[s[end]]-=1
			if dic[s[end]]==0:
				counter-=1
		end+=1

		while counter==0:
			if s[begin] in dic:
				dic[s[begin]]+=1
				if dic[s[begin]]>0:
					counter+=1
			if len(result)==0:
				result=s[begin:end]
			elif end-begin<len(result):
				result=s[begin:end]
			begin+=1
	return result










