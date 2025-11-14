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

class Solution:
    def levelOrder(self, root):
        
        arr =[]

        if not root:
            return arr

        queue = []
        queue.append(root)

        while len(queue)!=0:

            temp_arr = []
            for i in range(0,len(queue)):
                node = queue.pop(0)
                temp_arr.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            arr.append(temp_arr)
        return arr