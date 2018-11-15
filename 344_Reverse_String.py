"""

Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"

Example 2:

Input: "A man, a plan, a canal: Panama"
"""

def reverseString(s):
	result=list(s)
	i,j=0,len(s)-1
	while i<j:
		result[i],result[j]=result[j],result[i]
		i+=1
		j-=1
	return "".join(result)

	