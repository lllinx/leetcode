"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note:

    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.

Example 1:

Input: n = 3, k = 3
Output: "213"

Example 2:

Input: n = 4, k = 9
Output: "2314"

"""

def getPermutation(n,k):
	num=[i for i in range(1,n+1)]
	factorial=[]
	fact=1
	for i in range(1,n+1):
		fact*=i
		factorial.append(fact)
	res=""
	k-=1
	for i in range(1,n+1):
		index=k//factorial[n-i-1]
		res+=str(num[index])
		num.pop(index)
		k=k%factorial[n-i-1]
	return res



	




