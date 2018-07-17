"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false

Example 2:

Input: "aab"
Output: true

Example 3:

Input: "carerac"
Output: true
"""

def canPermutePalindrome(s):
	dic={}
	for i in s:
		if i in dic:
			dic[i]+=1
		else:
			dic[i]=1
	odd=0
	for i in dic:
		if dic[i]%2==1:
			odd+=1
	return odd<=1

	
