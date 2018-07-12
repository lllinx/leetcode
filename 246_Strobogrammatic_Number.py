"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true

Example 2:

Input:  "88"
Output: true

Example 3:

Input:  "962"
Output: false
"""

def isStrobogrammatic(num):
	dic={"0":"0","1":"1","6":"9","8":"8","9":"6"}
	num2=""
	for i in num:
		if i not in dic.keys():
			return False
		else:
			num2+=dic[i]
	return num2==num[::-1]


