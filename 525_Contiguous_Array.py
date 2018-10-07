"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1

"""

def findMaxLength(nums):
	max_len=0
	count=0
	hashmap={0:-1}
	for i in range(len(nums)):
		if i==0:
			count-=1
		else:
			count+=1
		if count in hashmap:
			max_len=max(max_len,i-hashmap[count])
		else:
			hashmap[count]=i
	return max_len