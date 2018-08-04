"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""

def longestPalindrome(s):
	def extend(x,left,right):
		result=x
		while left>=0 and right<len(s) and s[left]==s[right]:
			result=s[left:right+1]
			left-=1
			right+=1
		return result

	result=""
	for i in range(len(s)):
		if len(extend(s[i],i,i))>len(result):
			result=extend(s[i],i,i)
		if len(extend(s[i],i,i+1))>len(result):
			result=extend(s[i],i,i+1)
	return result



