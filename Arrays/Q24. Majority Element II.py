'''
Problem Statement:


Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?

Problem Type: Medium

Problem Link: https://leetcode.com/problems/majority-element-ii/description/



'''
from collections import Counter
import math
class Solution:
    def majorityElement(self, nums):
        
        flag = math.floor(len(nums)/3)
        dic = Counter(nums)
        result = []
        for k,v in dic.items():
            if v > flag:
                result.append(k)
        return result