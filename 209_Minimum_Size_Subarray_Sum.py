"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""
# brute force
def MinSubArrayLen(s,nums):
	result=len(nums)+1
	for i in range(len(nums)):
		sums=nums[i]
		if sums>=s:
			return 1
		else:
			for j in range(i+1,len(nums)):
				sums+=nums[j]
				if sums>=s:
					result=min(result,j-i+1)
					break
	return result

# two pointer
# time complexity N
def MinSubArrayLen2(s,nums):
	result=len(nums)+1
	i,j,sums=0,0,0
	while j<len(nums):
		sums+=nums[j]
		j+=1
		while sums>=s:
			result=min(result,j-i)
			sums-=nums[i]
			i+=1
	if result==len(nums)+1:
		return 0
	return result

def MinSubArrayLen3(s,nums):
	result=len(nums)+1
	sums=[0 for i in range(len(nums)+1)]
	for i in range(1,len(nums)+1):
		sums[i]=sums[i-1]+nums[i-1]
	def binarysearch(low,high,sums,find):
		while low<=high:
			mid=(low+high)//2
			if sums[mid]>=find:
				high=mid-1
			else:
				low=mid+1
		return low
	for i in range(len(nums)):
		end=binarysearch(i+1,len(sums)-1,sums,sums[i]+s)
		if end-i<result:
			result=end-i
	if result==len(nums)+1:
		return 0
	return result
	



















