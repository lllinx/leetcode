"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""
def validpalindrome(s):
	low,high=0,len(s)-1
	while low<high:
		if s[low]!=s[high]:
			one,two=s[low:high],s[low+1:high+1]
			return one==one[::-1] or two==two[::-1]
		low+=1
		high-=1
	return True
