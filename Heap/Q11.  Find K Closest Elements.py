'''
Problem Statement:

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]

 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

Problem Type: Medium

Problem Link: https://leetcode.com/problems/find-k-closest-elements/description/?envType=problem-list-v2&envId=heap


'''

import heapq

class Solution:
    def findClosestElements(self, arr, k, x):
        
        items = []
        for i,v in enumerate(arr):
            items.append((i,abs(v-x)))

        heap = []
        for i, (index,val) in enumerate(items):
            heapq.heappush(heap,(val,index))
        result = []
        while k != 0:
            result.append(arr[heapq.heappop(heap)[1]])
            k-=1
        result.sort()
        return result
       

        