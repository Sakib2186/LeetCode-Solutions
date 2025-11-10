'''
Problem Statement:

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Problem type: Easy

Problem link: https://leetcode.com/problems/path-sum/


'''

class Solution:
    def hasPathSum(self, root,target) -> bool:
        
        if not root:
            return False
        
        if (target - root.val) == 0  and root.left == None and root.right == None:
            return True
        return self.hasPathSum(root.left,target-root.val) or self.hasPathSum(root.right,target-root.val)
