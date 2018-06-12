"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

def lengthOfLastWord(s):
	length=0
	i=len(s)-1

	while i>=0:
		if s[i]!=" ":
			length+=1
			j=i-1
			while j>=0:
				if s[j]==" ":
					return length
				j-=1
				length+=1
		i-=1
		return length
	return length

