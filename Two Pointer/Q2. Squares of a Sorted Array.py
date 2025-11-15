'''
Problem Statement:

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Problem Type: Easy

Problem Link: https://leetcode.com/problems/squares-of-a-sorted-array/


'''

class Solution:
    def sortedSquares1(self, nums):
        
        #solution 1: Faster
        arr = []
        final_arr = []
        for i in nums:
            if i < 0:
                i = i * -1
            arr.append(i)
        arr.sort()
        for i in arr:
            final_arr.append(i**2)

        return final_arr
    
    def sortedSquares2(self, nums):
        
        #solution 2: Two Pointer
        if nums[0] >=0:
            return [x**2 for x in nums]

        first_arr = []
        rem_arr = []
        index = 0
        for i, v in enumerate(nums):
            if v<0:
                first_arr.append(abs(v))
                index+=1
            else:
                index = i
                break
        
        first_arr = list(reversed(first_arr))
        rem_arr = nums[index:len(nums)]

        a,b = 0,0
        result = []
        while a<len(first_arr) and b<len(rem_arr):

            if first_arr[a] < rem_arr[b]:
                result.append(first_arr[a])
                a+=1
            else:
                result.append(rem_arr[b])
                b+=1

        if a<len(first_arr):
            result.extend(first_arr[a:len(first_arr)])
        if b<len(rem_arr):
            result.extend(rem_arr[b:len(rem_arr)])

        return [i**2 for i in result]