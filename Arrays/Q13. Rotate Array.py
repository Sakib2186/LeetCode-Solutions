'''

Problem Statement:

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Problem Type: Medium

Problem Link: https://leetcode.com/problems/rotate-array/


'''
import heapq
class Solution:
    def rotate(self, nums, k) :
        """
        Do not return anything, modify nums in-place instead.
        """
        min_heap = []
        for i in range(len(nums)):
            new_pos = i + k
            if new_pos >= len(nums):
                new_pos = new_pos - len(nums)
            heapq.heappush(min_heap,(new_pos,nums[i]))
        print(min_heap)

        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        nums = result