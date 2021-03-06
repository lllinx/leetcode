"""
 Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers? 
"""
# time limit exceeded
def combinationSum4_basic(nums, target):
	def helper(nums, target, res):
		if target==0:
			return 1
		elif target<0:
			return 0
		res=0
		for num in nums:
			if target>=num:
				res+=helper(nums, target-num, res)
		return res
	return helper(nums,target,0)

# time limit exceeded	
def combinationSum_ad(nums, target):
	dp=[-1 for _ in range(target+1)]
	dp[0]=1
	def helper(nums,target,res):
		if dp[target]!=-1:
			return dp[target]
		res=0
		for i in range(len(nums)):
			if target>=nums[i]:
				res+=helper(nums,target-nums[i],res)
		dp[target]=res
		return res

	return helper(nums,target,0)

# correct solution
def combinationSum4(nums,target):
	comb=[0 for _ in range(target+1)]
	comb[0]=1

	for i in range(1,target+1):
		for j in range(0,len(nums)):
			if i>=nums[j]:
				comb[i]+=comb[i-nums[j]]
	return comb[target]















