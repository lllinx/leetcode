"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]

"""
def missingrange(nums,lower,upper):
	def getrange(res,n1,n2):
		if n1==n2:
			res.append(str(n1))
		else:
			res.append(str(n1)+"->"+str(n2))

	next=lower
	result=[]

	if not nums:
		getrange(result,lower,upper)
		return result
	for i in range(len(nums)):
		if nums[i]<next:
			continue
		if nums[i]==next:
			next+=1
			continue
		getrange(result,next,nums[i]-1)
		next=nums[i]+1
	if nums[-1]<upper:
		getrange(result,next,upper)
	return result
















