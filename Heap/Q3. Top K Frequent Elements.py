'''
Problem Statement:

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Problem Type: Medium

Problem Link: https://leetcode.com/problems/top-k-frequent-elements/description/


'''

import heapq
class Solution:
    def topKFrequent(self, nums, k):
        
        min_heap =[]
        dic = {}
        for num in nums:
            heapq.heappush(min_heap,num)
        
        while len(min_heap)>0:
            element = heapq.heappop(min_heap)
            if element in dic:
                dic[element] += 1
            else:
                dic[element] = 1

        return [x for x,v in list(dic.items())[0:k]]
