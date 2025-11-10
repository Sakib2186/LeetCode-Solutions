'''
Problem Statement:

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []

Problem type: Medium

Problem link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

'''
class Solution:
    def zigzagLevelOrder(self, root):

        arr = []
        if not root:
            return arr

        queue = []
        queue.append(root)
        count = 0

        while (len(queue)!=0):

            temp_arr = []
            for i in range(0,len(queue)):
                if count%2 == 1: #odd level (inserting from back)
                    node = queue.pop(0)
                    temp_arr.append(node.val)
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
                else:
                    node = queue.pop() #even level (inserting from front)
                    temp_arr.append(node.val)
                    if node.left:
                        queue.insert(0,node.left)
                    if node.right:
                        queue.insert(0,node.right)
            
            count +=1
            arr.append(temp_arr)

        return arr