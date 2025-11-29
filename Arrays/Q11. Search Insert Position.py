'''

Problem Statement:

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Problem Type: Easy

Problem Link: https://leetcode.com/problems/search-insert-position/description/


'''


class Solution:
    def searchInsert(self, nums, target) -> int:

        start = 0
        end = len(nums) - 1
        return self.binary_search(start,end,target,nums)

    def binary_search(self,start,end,target,nums):
        
        while start<=end:
            mid_index = (start+end)//2
            mid = nums[mid_index]
 
            if mid < target:
                start = mid_index + 1
    
            elif mid > target:
                end = mid_index - 1
            else:
                return mid_index

        return start
        