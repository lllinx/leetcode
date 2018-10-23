"""

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99

"""

def countNumbersWithUniqueDigits(n):
	if n==0:
		return 1
	res=10
	unique_digit=9
	avail_num=9

	while n>1 and avail_num>0:
		unique_digit*=avail_num
		res+=unique_digit
		avail_num-=1
		n-=1
	return res

	
