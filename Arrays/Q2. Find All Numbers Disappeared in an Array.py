'''
Problem Statement:

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

Problem Type: Easy

Problem Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

'''

class Solution:
    def findDisappearedNumbers(self, nums):
        
        set_arr = set(nums)
        arr = []
        for i in range(1,len(nums)+1):

            if i not in set_arr:
                arr.append(i)

        return arr