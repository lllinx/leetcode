"""4. Median of Two Sorted Arrays"""
def findMedianSortedArrays(nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: float
	"""
	def median(x):
		length=len(x)
		if length%2==0:
			return (x[length//2-1]+x[length//2])/2
		else:
			return x[(length-1)//2]
	if max(nums1)<min(nums2):
		new_list=nums1+nums2
	elif min(nums1)>max(nums2):
		new_list=nums2+nums1
	else:
		new_list=[]
		for el1 in list(nums1):
			for el2 in list(nums2):
				if el1<el2:
					new_list.append(el1)
					nums1.remove(el1)
				elif el1>el2:
					new_list.append(el2)
					nums2.remove(el2)
				elif el1==el2:
					new_list.extend([el1,el2])
					nums1.remove(el1)
					nums2.remove(el2)
	return median(new_list)