'''
Problem Statement:

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

Problem Type: Easy

Problem Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/




'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def find_match(l1,l2,starting_pos):
            i , j = starting_pos ,0 
            count = 0
            while i < len(l1) and j < len(l2):
                if l1[i] != l2[j]:
                    return False
                i += 1
                j += 1
                count += 1
            if count == len(l2):
                return True
            return False

        needle_list = list(needle)
        haystack_list = list(haystack)
        if len(haystack_list) < len(needle_list):
            return -1
        i = 0
        idx = []
        while i < len(haystack_list):
            if find_match(haystack_list,needle_list,i):
                idx.append(i)
            i += 1
        
        if idx:
            return idx[0]
        else:
            return -1
