"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

"""
def mysqrt(x):
	ans=x
	delta=0.01
	while abs(pow(ans,2)-x)>delta:
		ans=(ans+x/ans)/2
	return int(ans)

	