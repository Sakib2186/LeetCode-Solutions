'''
Problem Statement:


Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []


Problem Type: Medium

Problem Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/?envType=problem-list-v2&envId=arrays



'''

# First Solution
from collections import Counter
class Solution:
    def findDuplicates(self, nums):
        
        elements = Counter(nums)
        result = []
        for key,value in elements.items():
            if value == 2: 
                result.append(key)

        return result
    
# Second Solution

class Solution:
    def findDuplicates(self, nums):
        
        seen = set()
        result = []
        for x in nums:
            if x in seen:
                result.append(x)
            else:
                seen.add(x)
        return result