"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

def longestPalindrome(s):
	dic={}
	result,odd=0,0
	for ch in s:
		if ch not in dic:
			dic[ch]=1
		else:
			dic[ch]+=1

	for v in dic.values():
		if v%2==0:
			result+=v
		else:
			result+=v-1
			odd=1
	return result+odd







