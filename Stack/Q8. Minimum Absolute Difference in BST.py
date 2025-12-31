'''
Problem Statement:

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105

Problem Type: Easy

Problem Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/


'''

class Solution:

    def getMinimumDifference(self, root) -> int:

        minDiff = float('inf')
        prevVal = float('-inf')
        
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                minDiff = min(minDiff, root.val-prevVal)
                prevVal = root.val
                root = root.right
        
        return minDiff
