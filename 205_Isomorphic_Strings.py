"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
"""
def isIsomorphic(s,t):
	dic1, dic2={}, {}
	for i,j in zip(s,t):
		if (i in dic1 and dic1[i]!=j) or (j in dic2 and dic2[j]!=i):
			return False
		dic1[i], dic2[j]=j,i
	return True


