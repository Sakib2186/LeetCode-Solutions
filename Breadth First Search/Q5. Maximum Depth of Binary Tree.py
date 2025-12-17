'''
Problem Statement:

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

Problem type: Easy

Problem link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

'''

class Solution:
    def maxDepth(self, root) -> int:

        if not root:
            return 0

        count = 0
        queue = []
        queue.append(root)
        
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
            count += 1
        return count
        