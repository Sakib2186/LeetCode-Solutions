'''
Problem Statement:

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

Problem type: Medium

Problem link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

'''

class Solution:
    def levelOrderBottom(self, root):
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
        return arr[::-1]