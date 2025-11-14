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
        
        queue = []
        queue.append(root)
        count = 1
        while len(queue)!=0:

            i = len(queue)
            for i in range(0,i):
                element = queue.pop(0)

                if element.left==None and element.right == None:
                    return count
                
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            count +=1