'''
Problem Statement:

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Prblem type: Medium

Problem link: https://leetcode.com/problems/binary-tree-level-order-traversal/
'''
from collections import deque
class Solution:
    def levelOrder(self, root):
        
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
            result.append(level)
        return result