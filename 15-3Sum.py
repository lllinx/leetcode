def threesum(nums):
	nums.sort()
	result=[]
	for i in range(len(nums)-2):
		if nums[i]>0:
			break
		if i>=1 and nums[i]==nums[i-1]:
			continue
		target=-nums[i]
		l,r=i+1,len(nums)-1
		while l<r:
			if nums[l]+nums[r]==target:
				result.append([nums[i],nums[l],nums[r]])
				while l<r and nums[l+1]==nums[l]:
					l+=1
				l+=1
				while l<r and nums[r-1]==nums[r]:
					r-=1
				r-=1
			elif nums[l]+nums[r]>target:
				while l<r and nums[l+1]==nums[l]:
					l+=1
				l+=1
			else:
				while l<r and nums[r-1]==nums[r]:
					r-=1
				r-=1
	return result


