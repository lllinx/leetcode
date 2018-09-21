"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

"""

def summaryRanges(nums):
	result=[]
	start,end=0,0
	while end<len(nums):
		if end<len(nums)-1 and nums[end+1]-nums[end]==1:
			end+=1
		else:
			if end-start>0:
				result.append(str(nums[start])+"->"+str(nums[end]))
			else:
				result.append(str(nums[start]))
			start=end+1
			end=start
	return result



