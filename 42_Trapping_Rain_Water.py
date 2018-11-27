"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""
# brute force time n^2, space 1
def trap(height):
	result=0
	for i in range(1,len(height)-1):
		left=max(height[:i+1])
		right=max(height[i:])
		result+=min(left,right)-height[i]
	return result

# dp time n, space n
def trap_dp(height):
	if not height:
		return 0

	result=0
	left_max=[0 for _ in range(len(height))]
	right_max=[0 for _ in range(len(height))]
	left_max[0]=height[0]
	right_max[-1]=height[-1]

	for i in range(1,len(height)):
		left_max[i]=max(left_max[i-1],height[i])
	for j in range(len(height)-2,-1,-1):
		right_max[j]=max(right_max[j+1],height[j])
	for i in range(1,len(height)-1):
		result+=min(left_max[i],right_max[i])-height[i]
	return result

# two pointer time n, space 1
def trap_two_pointer1(height):
	l,r=0,len(height)-1
	result=0
	leftmax,rightmax=0,0

	while l<r:
		if height[l]<height[r]:
			leftmax=max(leftmax,height[l])
			result+=leftmax-height[l]
			l+=1
		else:
			rightmax=max(rightmax,height[r])
			result+=rightmax-height[r]
			r-=1
	return result

def trap_two_pointer2(height):
	l,r=0,len(height)-1
	result=0
	leftmax,rightmax=0,0

	while l<r:
		if height[l]<height[r]:
			if leftmax<height[l]:
				leftmax=height[l]
			else:
				result+=leftmax-height[l]
			l+=1
		else:
			if rightmax<height[r]:
				rightmax=height[r]
			else:
				result+=rightmax-height[r]
			r-=1
	return result


# stack














