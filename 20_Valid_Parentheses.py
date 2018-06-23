"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

def isValid(s):
	stack=[]
	dic={"]":"[",")":"(","}":"{"}
	for i in s:
		if i in dic.values():
			stack.append(i)
		elif i in dic.keys() and stack and stack[-1]==dic[i]:
			stack.pop()
		else:
			return False

	return stack==[]
	




