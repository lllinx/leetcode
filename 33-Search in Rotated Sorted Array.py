"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            if nums[l]<=nums[m]:
                if nums[l]<=target and target<=nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                if nums[m]<=target and target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        return -1
                
            