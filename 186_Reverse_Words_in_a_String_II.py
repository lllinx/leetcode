"""

Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Note: 

    A word is defined as a sequence of non-space characters.
    The input string does not contain leading or trailing spaces.
    The words are always separated by a single space.

Follow up: Could you do it in-place without allocating extra space?
"""

def reverseWords(string):
	def reverse(s,start,end):
		while start<end:
			s[start],s[end]=s[end],s[start]
			start+=1
			end-=1

	reverse(string,0,len(string)-1)
	first,step=0,0
	while step<len(string):
		if string[step]==" ":
			reverse(string,first,step-1)
			first=step+1
		if step==len(string)-1:
			reverse(string,first,step)
		step+=1
	return string

	








		
