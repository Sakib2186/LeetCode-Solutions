'''

Problem Statement:

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Problem Type: Easy


Problem Link: https://leetcode.com/problems/intersection-of-two-arrays/




'''

class Solution:
    def intersection(self, nums1, nums2):
        
        dic = {}
        result = set()
        a1 = len(nums1)
        a2 = len(nums2)

        if a1 < a2:
            for i in nums1:
                dic[i] = '#'
            for i in nums2:
                if i in dic:
                    result.add(i)
        else:
            for i in nums2:
                dic[i] = '#'
            for i in nums1:
                if i in dic:
                    result.add(i)
        return list(result)

# Could be optimized
        
