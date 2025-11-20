'''

Problem Statement:

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
 

Problem Type: Easy

Problem Link: https://leetcode.com/problems/minimum-absolute-difference/

'''

class Solution:
    def minimumAbsDifference1(self, arr):

        result = []
        arr_len = len(arr)
        min_val = 999999
        arr.sort()
        for i in range(1,arr_len):

            prev_index = i-1
            min_val = min(min_val,abs(arr[i]-arr[prev_index]))
        
        for i in range(1,arr_len):

            prev_index = i-1
            if abs(arr[i]-arr[prev_index]) == min_val:
                result.append([arr[prev_index],arr[i]])

        return result
        