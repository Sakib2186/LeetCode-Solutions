'''
Problem Statement:

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Problem Type: Hard

Problem Link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/



'''
import math
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i,j = 0,0
        arr = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            arr.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            arr.append(nums2[j])
            j += 1
        
        final_len = len(arr)

        if final_len == 0:
            return 0

        if final_len % 2 == 0:
            index = final_len // 2
            return (arr[index] + arr[index - 1]) / 2
        else:
            index = math.floor(final_len // 2)
            return arr[index]

# Time Complexity: O(m + n)