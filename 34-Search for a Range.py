"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

def searchRange(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                index1,index2=m,m
                while index1>0 and nums[index1]==nums[index1-1]:
                    index1-=1
                while index2<r and nums[index2]==nums[index2+1]:
                    index2+=1
                return [index1,index2]
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        return [-1,-1]
        