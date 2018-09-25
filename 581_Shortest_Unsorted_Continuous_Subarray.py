"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:

    Then length of the input array is in range [1, 10,000].
    The input array may contain duplicates, so ascending order here means <=.
"""

def findUnsortedSubarray(nums):
	num=sorted(nums)
	start,end=None,None
	for i in range(len(num)):
		if start is None and num[i]!=nums[i]:
			start=i
		if num[i]!=nums[i]:
			end=i
	if not start and not end:
		return 0
	return end-start+1


def findUnsortedSubarray2(nums):
	start,end=-1,-2
	maxi,mini=nums[0],nums[-1]
	n=len(nums)
	for i in range(len(nums)):
		maxi=max(maxi,nums[i])
		mini=min(mini,nums[n-1-i])
		if nums[i]<maxi:
			end=i
		if nums[n-1-i]>mini:
			start=n-1-i
	return end-start+1











