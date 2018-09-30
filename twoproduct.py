"""
two multiply

give a list of unsorted integer, including positive and negative values
which may include duplicate values
list the pair of integers which has a product of k

eg:
[-1,-2,-6,3,4,2,8,1,-12], k=12
output:
[[-1,-12],[-2,-6],[3,4]]

eg:
[-1,-2,-6,3,4,2,8,1,-12,3,4,4]
output:
[[-1,-12],[-2,-6],[3,4]]

"""

def twoproduct(nums,k):
	dic={}
	result=set()
	for i in range(len(nums)):
		if k%nums[i]!=0:
			continue
		else:
			if nums[i] in dic:
				result.add((nums[i],k//nums[i]))
			else:
				dic[k//nums[i]]=i
	return result



