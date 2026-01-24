'''
Problem Statement:

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

Problem Type: Medium

Problem Link: https://leetcode.com/problems/reorganize-string/



'''
import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = Counter(s)
        max_heap = []
        for k,v in dic.items():
            heapq.heappush(max_heap,(-v,k))

        result = ""
        while len(max_heap)>1:
            v1,k1 = heapq.heappop(max_heap)
            v2,k2 = heapq.heappop(max_heap)
            v1 = -v1
            v2 = -v2

            result += k1
            v1 -= 1
            result += k2
            v2 -= 1
            if v1 > 0:
                heapq.heappush(max_heap,(-v1,k1))
            if v2 > 0:
                heapq.heappush(max_heap,(-v2,k2))
         
        if len(max_heap) == 0:
            return result
        elif len(max_heap) == 1:
            v,k = heapq.heappop(max_heap)
            if -v == 1:
                result += k
                return result
            else:
                return ""
        else:
            return ""
