'''
Problem Statement:

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Problem type: Easy

Problem link: https://leetcode.com/problems/minimum-depth-of-binary-tree/

'''

class Solution:
    def minDepth(self, root) -> int:
        
        if not root:
            return 0

        count = 0
        queue = []
        queue.append(root)

        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:
                    count+=1
                    return count
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            count += 1