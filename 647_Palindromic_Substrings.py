"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

def countSubstrings(s):
	begin=0
	result=[]
	while begin<len(s):
		end=begin+1
		while end<len(s)+1:
			if s[begin:end]==s[begin:end][::-1]:
				result.append(s[begin:end])
			end+=1
		begin+=1
	return len(result)


def countSubstrings2(s):
	def extend(x,left,right):
		count=0
		while left>=0 and right<len(s) and s[left]==s[right]:
			count+=1
			left-=1
			right+=1
		return count
	
	if len(s)==0:
		return 0
	count=0
	for i in range(len(s)):
		count+=extend(s[i],i,i)
		count+=extend(s[i],i,i+1)
	return count

	
	




